from collections import defaultdict
import curses
from curses import tigetstr, setupterm, tparm
from fcntl import ioctl
from os import isatty, environ
import struct
import sys
from termios import TIOCGWINSZ


__all__ = ['Terminal']


class Terminal(object):
    """An abstraction around terminal capabilities

    Unlike curses, this doesn't require clearing the screen before doing
    anything, and it's a little friendlier to use. It keeps the endless calls
    to tigetstr() and tparm() out of your code, and it acts intelligently when
    somebody pipes your output to a non-terminal.

    """
    def __init__(self, kind=None, stream=None):
        """Initialize the terminal.

        :arg kind: A terminal string as taken by setupterm(). Defaults to the
            value of the TERM environment variable.
        :arg stream: A file-like object representing the terminal. Defaults to
            the original value of stdout, like ``curses.initscr()`` does.

        If ``stream`` is not a tty, I will default to returning '' for all
        capability values, so things like piping your output to a file will
        work nicely.

        """
        if stream is None:
            stream = sys.__stdout__
        if (hasattr(stream, 'fileno') and
            callable(stream.fileno) and
            isatty(stream.fileno())):
            # Make things like tigetstr() work:
            # (Explicit args make setupterm() work even when -s is passed.)
            setupterm(kind or environ.get('TERM', 'unknown'),
                      stream.fileno())
            # Cache capability codes, because IIRC tigetstr requires a
            # conversation with the terminal. [Now I can't find any evidence of
            # that.]
            self._codes = {}
        else:
            self._codes = NullDict(lambda: '')

        # It's convenient to pass the stream around with the terminal; it's
        # almost always needed when the terminal is and saves sticking lots of
        # extra args on things in practice.
        self.stream = stream

    # Sugary names for commonly-used capabilities, intended to help avoid trips
    # to the terminfo man page and comments in your code:
    _sugar = dict(save='sc',
                  restore='rc',

                  clear_eol='el',
                  position='cup',

                  # You can use these if you want, but the named equivalents
                  # like "red" and "bg_green" are probably easier.
                  color='setaf',
                  bg_color='setab',

                  normal='sgr0',
                  reverse='rev',
                  # 'bold' is just 'bold'.
                  underline='smul',
                  no_underline='rmul')

    def _color(self, color):
        return (self.setaf or self.setf)(color)

    def _bg_color(self, color):
        return (self.setab or self.setb)(color)

    def __getattr__(self, attr):
        """Return parametrized terminal capabilities, like bold.

        For example, you can say ``some_term.bold`` to get the string that
        turns on bold formatting and ``some_term.sgr0`` to get the string that
        turns it off again. For a parametrized capability like ``cup``, pass
        the parameter too: ``some_term.cup(line, column)``.

        ``man terminfo`` for a complete list of capabilities.

        """
        if attr not in self._codes:
            # Store sugary names under the sugary keys to save a hash lookup.
            # Fall back to '' for codes not supported by this terminal.
            self._codes[attr] = tigetstr(self._sugar.get(attr, attr)) or ''
        return CallableString(self._codes[attr])

    @property
    def height(self):
        return height_and_width()[0]

    @property
    def width(self):
        return height_and_width()[1]

    def location(self, x, y):
        """Return a context manager for temporarily moving the cursor

        Move the cursor to a certain position on entry, let you print stuff
        there, then return the cursor to its original position::

            term = Terminal()
            with term.position(2, 5):
                print 'Hello, world!'
                for x in xrange(10):
                    print 'I can do it %i times!' % x

        """
        return Location(x, y, self)


def _add_color_methods():  # Really, really private
    """Return an iterable of method pairs that set fg and bg colors.

    The methods in the pair return the escape sequences to set the foreground
    or background color, respectively.

    """
    # TODO: Does curses automatically exchange red and blue and cyan and yellow
    # when a terminal supports setf/setb rather than setaf/setab? I'll be
    # blasted if I can find any documentation. The following assumes it does.
    def colorers(color, offset=0):
        """Return a method that returns the formatting string to set a certain color.

        curses constants go up to only 7, so pass in an offset to get at the
        bright colors at 8-15.

        """
        const = 'COLOR_' + color.upper()

        @property
        def some_color(self):
            return self._color(getattr(curses, const) + offset)

        @property
        def some_bg_color(self):
            return self._bg_color(getattr(curses, const) + offset)

        return some_color, some_bg_color

    for color in ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']:
        # Foreground and background:
        fg_method, bg_method = colorers(color)
        setattr(Terminal, color, fg_method)
        setattr(Terminal, 'bg_' + color, bg_method)

        # Foreground and background, bright:
        fg_method, bg_method = colorers(color, offset=8)
        setattr(Terminal, 'bright_' + color, fg_method)
        setattr(Terminal, 'bg_bright_' + color, bg_method)


# Add color and background color attrs, like red and bg_red:
_add_color_methods()


class CallableString(str):
    """A string which can be called to parametrize it as a terminal capability"""
    def __call__(self, *args):
        try:
            return tparm(self, *args)
        except curses.error:
            # Catch "must call (at least) setupterm() first" errors, as when
            # running simply `nosetests` (without progressive) on nose-
            # progressive. Perhaps the terminal has gone away between calling
            # tigetstr and calling tparm.
            return ''


class NullDict(defaultdict):
    """A ``defaultdict`` that pretends to contain all keys"""
    def __contains__(self, key):
        return True


def height_and_width():
    """Return a tuple of (terminal height, terminal width)."""
    # tigetnum('lines') and tigetnum('cols') apparently don't update while
    # nose-progressive's progress bar is running.
    return struct.unpack('hhhh', ioctl(0, TIOCGWINSZ, '\000' * 8))[0:2]


class Location(object):
    """Context manager for temporarily moving the cursor"""
    def __init__(self, x, y, term):
        self.x, self.y = x, y
        self.term = term

    def __enter__(self):
        """Save position and move to progress bar, col 1."""
        self.term.stream.write(self.term.save)  # save position
        self.term.stream.write(self.term.position(self.y, self.x))

    def __exit__(self, type, value, tb):
        self.term.stream.write(self.term.restore)  # restore position
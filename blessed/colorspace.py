"""
References,

- https://github.com/freedesktop/xorg-rgb/blob/master/rgb.txt
- https://github.com/ThomasDickey/xterm-snapshots/blob/master/256colres.h
- https://github.com/ThomasDickey/xterm-snapshots/blob/master/XTerm-col.ad
- https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
- https://gist.github.com/XVilka/8346728
- https://devblogs.microsoft.com/commandline/24-bit-color-in-the-windows-console/
- http://jdebp.eu/Softwares/nosh/guide/TerminalCapabilities.html
"""
# std imports
import collections

__all__ = (
    'CGA_COLORS',
    'RGBColor',
    'RGB_256TABLE',
    'X11_COLORNAMES_TO_RGB',
)

CGA_COLORS = set(
    ('black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'))


class RGBColor(collections.namedtuple("RGBColor", ["red", "green", "blue"])):
    def __str__(self):
        return '#{0:02x}{1:02x}{2:02x}'.format(*self)


#: X11 Color names to (XTerm-defined) RGB values from xorg-rgb/rgb.txt
X11_COLORNAMES_TO_RGB = {
    'aliceblue': RGBColor(240, 248, 255),
    'antiquewhite': RGBColor(250, 235, 215),
    'antiquewhite1': RGBColor(255, 239, 219),
    'antiquewhite2': RGBColor(238, 223, 204),
    'antiquewhite3': RGBColor(205, 192, 176),
    'antiquewhite4': RGBColor(139, 131, 120),
    'aqua': RGBColor(0, 255, 255),
    'aquamarine': RGBColor(127, 255, 212),
    'aquamarine1': RGBColor(127, 255, 212),
    'aquamarine2': RGBColor(118, 238, 198),
    'aquamarine3': RGBColor(102, 205, 170),
    'aquamarine4': RGBColor(69, 139, 116),
    'azure': RGBColor(240, 255, 255),
    'azure1': RGBColor(240, 255, 255),
    'azure2': RGBColor(224, 238, 238),
    'azure3': RGBColor(193, 205, 205),
    'azure4': RGBColor(131, 139, 139),
    'beige': RGBColor(245, 245, 220),
    'bisque': RGBColor(255, 228, 196),
    'bisque1': RGBColor(255, 228, 196),
    'bisque2': RGBColor(238, 213, 183),
    'bisque3': RGBColor(205, 183, 158),
    'bisque4': RGBColor(139, 125, 107),
    'black': RGBColor(0, 0, 0),
    'blanchedalmond': RGBColor(255, 235, 205),
    'blue': RGBColor(0, 0, 255),
    'blue1': RGBColor(0, 0, 255),
    'blue2': RGBColor(0, 0, 238),
    'blue3': RGBColor(0, 0, 205),
    'blue4': RGBColor(0, 0, 139),
    'blueviolet': RGBColor(138, 43, 226),
    'brown': RGBColor(165, 42, 42),
    'brown1': RGBColor(255, 64, 64),
    'brown2': RGBColor(238, 59, 59),
    'brown3': RGBColor(205, 51, 51),
    'brown4': RGBColor(139, 35, 35),
    'burlywood': RGBColor(222, 184, 135),
    'burlywood1': RGBColor(255, 211, 155),
    'burlywood2': RGBColor(238, 197, 145),
    'burlywood3': RGBColor(205, 170, 125),
    'burlywood4': RGBColor(139, 115, 85),
    'cadetblue': RGBColor(95, 158, 160),
    'cadetblue1': RGBColor(152, 245, 255),
    'cadetblue2': RGBColor(142, 229, 238),
    'cadetblue3': RGBColor(122, 197, 205),
    'cadetblue4': RGBColor(83, 134, 139),
    'chartreuse': RGBColor(127, 255, 0),
    'chartreuse1': RGBColor(127, 255, 0),
    'chartreuse2': RGBColor(118, 238, 0),
    'chartreuse3': RGBColor(102, 205, 0),
    'chartreuse4': RGBColor(69, 139, 0),
    'chocolate': RGBColor(210, 105, 30),
    'chocolate1': RGBColor(255, 127, 36),
    'chocolate2': RGBColor(238, 118, 33),
    'chocolate3': RGBColor(205, 102, 29),
    'chocolate4': RGBColor(139, 69, 19),
    'coral': RGBColor(255, 127, 80),
    'coral1': RGBColor(255, 114, 86),
    'coral2': RGBColor(238, 106, 80),
    'coral3': RGBColor(205, 91, 69),
    'coral4': RGBColor(139, 62, 47),
    'cornflowerblue': RGBColor(100, 149, 237),
    'cornsilk': RGBColor(255, 248, 220),
    'cornsilk1': RGBColor(255, 248, 220),
    'cornsilk2': RGBColor(238, 232, 205),
    'cornsilk3': RGBColor(205, 200, 177),
    'cornsilk4': RGBColor(139, 136, 120),
    'crimson': RGBColor(220, 20, 60),
    'cyan': RGBColor(0, 255, 255),
    'cyan1': RGBColor(0, 255, 255),
    'cyan2': RGBColor(0, 238, 238),
    'cyan3': RGBColor(0, 205, 205),
    'cyan4': RGBColor(0, 139, 139),
    'darkblue': RGBColor(0, 0, 139),
    'darkcyan': RGBColor(0, 139, 139),
    'darkgoldenrod': RGBColor(184, 134, 11),
    'darkgoldenrod1': RGBColor(255, 185, 15),
    'darkgoldenrod2': RGBColor(238, 173, 14),
    'darkgoldenrod3': RGBColor(205, 149, 12),
    'darkgoldenrod4': RGBColor(139, 101, 8),
    'darkgray': RGBColor(169, 169, 169),
    'darkgreen': RGBColor(0, 100, 0),
    'darkgrey': RGBColor(169, 169, 169),
    'darkkhaki': RGBColor(189, 183, 107),
    'darkmagenta': RGBColor(139, 0, 139),
    'darkolivegreen': RGBColor(85, 107, 47),
    'darkolivegreen1': RGBColor(202, 255, 112),
    'darkolivegreen2': RGBColor(188, 238, 104),
    'darkolivegreen3': RGBColor(162, 205, 90),
    'darkolivegreen4': RGBColor(110, 139, 61),
    'darkorange': RGBColor(255, 140, 0),
    'darkorange1': RGBColor(255, 127, 0),
    'darkorange2': RGBColor(238, 118, 0),
    'darkorange3': RGBColor(205, 102, 0),
    'darkorange4': RGBColor(139, 69, 0),
    'darkorchid': RGBColor(153, 50, 204),
    'darkorchid1': RGBColor(191, 62, 255),
    'darkorchid2': RGBColor(178, 58, 238),
    'darkorchid3': RGBColor(154, 50, 205),
    'darkorchid4': RGBColor(104, 34, 139),
    'darkred': RGBColor(139, 0, 0),
    'darksalmon': RGBColor(233, 150, 122),
    'darkseagreen': RGBColor(143, 188, 143),
    'darkseagreen1': RGBColor(193, 255, 193),
    'darkseagreen2': RGBColor(180, 238, 180),
    'darkseagreen3': RGBColor(155, 205, 155),
    'darkseagreen4': RGBColor(105, 139, 105),
    'darkslateblue': RGBColor(72, 61, 139),
    'darkslategray': RGBColor(47, 79, 79),
    'darkslategray1': RGBColor(151, 255, 255),
    'darkslategray2': RGBColor(141, 238, 238),
    'darkslategray3': RGBColor(121, 205, 205),
    'darkslategray4': RGBColor(82, 139, 139),
    'darkslategrey': RGBColor(47, 79, 79),
    'darkturquoise': RGBColor(0, 206, 209),
    'darkviolet': RGBColor(148, 0, 211),
    'deeppink': RGBColor(255, 20, 147),
    'deeppink1': RGBColor(255, 20, 147),
    'deeppink2': RGBColor(238, 18, 137),
    'deeppink3': RGBColor(205, 16, 118),
    'deeppink4': RGBColor(139, 10, 80),
    'deepskyblue': RGBColor(0, 191, 255),
    'deepskyblue1': RGBColor(0, 191, 255),
    'deepskyblue2': RGBColor(0, 178, 238),
    'deepskyblue3': RGBColor(0, 154, 205),
    'deepskyblue4': RGBColor(0, 104, 139),
    'dimgray': RGBColor(105, 105, 105),
    'dimgrey': RGBColor(105, 105, 105),
    'dodgerblue': RGBColor(30, 144, 255),
    'dodgerblue1': RGBColor(30, 144, 255),
    'dodgerblue2': RGBColor(28, 134, 238),
    'dodgerblue3': RGBColor(24, 116, 205),
    'dodgerblue4': RGBColor(16, 78, 139),
    'firebrick': RGBColor(178, 34, 34),
    'firebrick1': RGBColor(255, 48, 48),
    'firebrick2': RGBColor(238, 44, 44),
    'firebrick3': RGBColor(205, 38, 38),
    'firebrick4': RGBColor(139, 26, 26),
    'floralwhite': RGBColor(255, 250, 240),
    'forestgreen': RGBColor(34, 139, 34),
    'fuchsia': RGBColor(255, 0, 255),
    'gainsboro': RGBColor(220, 220, 220),
    'ghostwhite': RGBColor(248, 248, 255),
    'gold': RGBColor(255, 215, 0),
    'gold1': RGBColor(255, 215, 0),
    'gold2': RGBColor(238, 201, 0),
    'gold3': RGBColor(205, 173, 0),
    'gold4': RGBColor(139, 117, 0),
    'goldenrod': RGBColor(218, 165, 32),
    'goldenrod1': RGBColor(255, 193, 37),
    'goldenrod2': RGBColor(238, 180, 34),
    'goldenrod3': RGBColor(205, 155, 29),
    'goldenrod4': RGBColor(139, 105, 20),
    'gray': RGBColor(190, 190, 190),
    'gray0': RGBColor(0, 0, 0),
    'gray1': RGBColor(3, 3, 3),
    'gray10': RGBColor(26, 26, 26),
    'gray100': RGBColor(255, 255, 255),
    'gray11': RGBColor(28, 28, 28),
    'gray12': RGBColor(31, 31, 31),
    'gray13': RGBColor(33, 33, 33),
    'gray14': RGBColor(36, 36, 36),
    'gray15': RGBColor(38, 38, 38),
    'gray16': RGBColor(41, 41, 41),
    'gray17': RGBColor(43, 43, 43),
    'gray18': RGBColor(46, 46, 46),
    'gray19': RGBColor(48, 48, 48),
    'gray2': RGBColor(5, 5, 5),
    'gray20': RGBColor(51, 51, 51),
    'gray21': RGBColor(54, 54, 54),
    'gray22': RGBColor(56, 56, 56),
    'gray23': RGBColor(59, 59, 59),
    'gray24': RGBColor(61, 61, 61),
    'gray25': RGBColor(64, 64, 64),
    'gray26': RGBColor(66, 66, 66),
    'gray27': RGBColor(69, 69, 69),
    'gray28': RGBColor(71, 71, 71),
    'gray29': RGBColor(74, 74, 74),
    'gray3': RGBColor(8, 8, 8),
    'gray30': RGBColor(77, 77, 77),
    'gray31': RGBColor(79, 79, 79),
    'gray32': RGBColor(82, 82, 82),
    'gray33': RGBColor(84, 84, 84),
    'gray34': RGBColor(87, 87, 87),
    'gray35': RGBColor(89, 89, 89),
    'gray36': RGBColor(92, 92, 92),
    'gray37': RGBColor(94, 94, 94),
    'gray38': RGBColor(97, 97, 97),
    'gray39': RGBColor(99, 99, 99),
    'gray4': RGBColor(10, 10, 10),
    'gray40': RGBColor(102, 102, 102),
    'gray41': RGBColor(105, 105, 105),
    'gray42': RGBColor(107, 107, 107),
    'gray43': RGBColor(110, 110, 110),
    'gray44': RGBColor(112, 112, 112),
    'gray45': RGBColor(115, 115, 115),
    'gray46': RGBColor(117, 117, 117),
    'gray47': RGBColor(120, 120, 120),
    'gray48': RGBColor(122, 122, 122),
    'gray49': RGBColor(125, 125, 125),
    'gray5': RGBColor(13, 13, 13),
    'gray50': RGBColor(127, 127, 127),
    'gray51': RGBColor(130, 130, 130),
    'gray52': RGBColor(133, 133, 133),
    'gray53': RGBColor(135, 135, 135),
    'gray54': RGBColor(138, 138, 138),
    'gray55': RGBColor(140, 140, 140),
    'gray56': RGBColor(143, 143, 143),
    'gray57': RGBColor(145, 145, 145),
    'gray58': RGBColor(148, 148, 148),
    'gray59': RGBColor(150, 150, 150),
    'gray6': RGBColor(15, 15, 15),
    'gray60': RGBColor(153, 153, 153),
    'gray61': RGBColor(156, 156, 156),
    'gray62': RGBColor(158, 158, 158),
    'gray63': RGBColor(161, 161, 161),
    'gray64': RGBColor(163, 163, 163),
    'gray65': RGBColor(166, 166, 166),
    'gray66': RGBColor(168, 168, 168),
    'gray67': RGBColor(171, 171, 171),
    'gray68': RGBColor(173, 173, 173),
    'gray69': RGBColor(176, 176, 176),
    'gray7': RGBColor(18, 18, 18),
    'gray70': RGBColor(179, 179, 179),
    'gray71': RGBColor(181, 181, 181),
    'gray72': RGBColor(184, 184, 184),
    'gray73': RGBColor(186, 186, 186),
    'gray74': RGBColor(189, 189, 189),
    'gray75': RGBColor(191, 191, 191),
    'gray76': RGBColor(194, 194, 194),
    'gray77': RGBColor(196, 196, 196),
    'gray78': RGBColor(199, 199, 199),
    'gray79': RGBColor(201, 201, 201),
    'gray8': RGBColor(20, 20, 20),
    'gray80': RGBColor(204, 204, 204),
    'gray81': RGBColor(207, 207, 207),
    'gray82': RGBColor(209, 209, 209),
    'gray83': RGBColor(212, 212, 212),
    'gray84': RGBColor(214, 214, 214),
    'gray85': RGBColor(217, 217, 217),
    'gray86': RGBColor(219, 219, 219),
    'gray87': RGBColor(222, 222, 222),
    'gray88': RGBColor(224, 224, 224),
    'gray89': RGBColor(227, 227, 227),
    'gray9': RGBColor(23, 23, 23),
    'gray90': RGBColor(229, 229, 229),
    'gray91': RGBColor(232, 232, 232),
    'gray92': RGBColor(235, 235, 235),
    'gray93': RGBColor(237, 237, 237),
    'gray94': RGBColor(240, 240, 240),
    'gray95': RGBColor(242, 242, 242),
    'gray96': RGBColor(245, 245, 245),
    'gray97': RGBColor(247, 247, 247),
    'gray98': RGBColor(250, 250, 250),
    'gray99': RGBColor(252, 252, 252),
    'green': RGBColor(0, 255, 0),
    'green1': RGBColor(0, 255, 0),
    'green2': RGBColor(0, 238, 0),
    'green3': RGBColor(0, 205, 0),
    'green4': RGBColor(0, 139, 0),
    'greenyellow': RGBColor(173, 255, 47),
    'grey': RGBColor(190, 190, 190),
    'grey0': RGBColor(0, 0, 0),
    'grey1': RGBColor(3, 3, 3),
    'grey10': RGBColor(26, 26, 26),
    'grey100': RGBColor(255, 255, 255),
    'grey11': RGBColor(28, 28, 28),
    'grey12': RGBColor(31, 31, 31),
    'grey13': RGBColor(33, 33, 33),
    'grey14': RGBColor(36, 36, 36),
    'grey15': RGBColor(38, 38, 38),
    'grey16': RGBColor(41, 41, 41),
    'grey17': RGBColor(43, 43, 43),
    'grey18': RGBColor(46, 46, 46),
    'grey19': RGBColor(48, 48, 48),
    'grey2': RGBColor(5, 5, 5),
    'grey20': RGBColor(51, 51, 51),
    'grey21': RGBColor(54, 54, 54),
    'grey22': RGBColor(56, 56, 56),
    'grey23': RGBColor(59, 59, 59),
    'grey24': RGBColor(61, 61, 61),
    'grey25': RGBColor(64, 64, 64),
    'grey26': RGBColor(66, 66, 66),
    'grey27': RGBColor(69, 69, 69),
    'grey28': RGBColor(71, 71, 71),
    'grey29': RGBColor(74, 74, 74),
    'grey3': RGBColor(8, 8, 8),
    'grey30': RGBColor(77, 77, 77),
    'grey31': RGBColor(79, 79, 79),
    'grey32': RGBColor(82, 82, 82),
    'grey33': RGBColor(84, 84, 84),
    'grey34': RGBColor(87, 87, 87),
    'grey35': RGBColor(89, 89, 89),
    'grey36': RGBColor(92, 92, 92),
    'grey37': RGBColor(94, 94, 94),
    'grey38': RGBColor(97, 97, 97),
    'grey39': RGBColor(99, 99, 99),
    'grey4': RGBColor(10, 10, 10),
    'grey40': RGBColor(102, 102, 102),
    'grey41': RGBColor(105, 105, 105),
    'grey42': RGBColor(107, 107, 107),
    'grey43': RGBColor(110, 110, 110),
    'grey44': RGBColor(112, 112, 112),
    'grey45': RGBColor(115, 115, 115),
    'grey46': RGBColor(117, 117, 117),
    'grey47': RGBColor(120, 120, 120),
    'grey48': RGBColor(122, 122, 122),
    'grey49': RGBColor(125, 125, 125),
    'grey5': RGBColor(13, 13, 13),
    'grey50': RGBColor(127, 127, 127),
    'grey51': RGBColor(130, 130, 130),
    'grey52': RGBColor(133, 133, 133),
    'grey53': RGBColor(135, 135, 135),
    'grey54': RGBColor(138, 138, 138),
    'grey55': RGBColor(140, 140, 140),
    'grey56': RGBColor(143, 143, 143),
    'grey57': RGBColor(145, 145, 145),
    'grey58': RGBColor(148, 148, 148),
    'grey59': RGBColor(150, 150, 150),
    'grey6': RGBColor(15, 15, 15),
    'grey60': RGBColor(153, 153, 153),
    'grey61': RGBColor(156, 156, 156),
    'grey62': RGBColor(158, 158, 158),
    'grey63': RGBColor(161, 161, 161),
    'grey64': RGBColor(163, 163, 163),
    'grey65': RGBColor(166, 166, 166),
    'grey66': RGBColor(168, 168, 168),
    'grey67': RGBColor(171, 171, 171),
    'grey68': RGBColor(173, 173, 173),
    'grey69': RGBColor(176, 176, 176),
    'grey7': RGBColor(18, 18, 18),
    'grey70': RGBColor(179, 179, 179),
    'grey71': RGBColor(181, 181, 181),
    'grey72': RGBColor(184, 184, 184),
    'grey73': RGBColor(186, 186, 186),
    'grey74': RGBColor(189, 189, 189),
    'grey75': RGBColor(191, 191, 191),
    'grey76': RGBColor(194, 194, 194),
    'grey77': RGBColor(196, 196, 196),
    'grey78': RGBColor(199, 199, 199),
    'grey79': RGBColor(201, 201, 201),
    'grey8': RGBColor(20, 20, 20),
    'grey80': RGBColor(204, 204, 204),
    'grey81': RGBColor(207, 207, 207),
    'grey82': RGBColor(209, 209, 209),
    'grey83': RGBColor(212, 212, 212),
    'grey84': RGBColor(214, 214, 214),
    'grey85': RGBColor(217, 217, 217),
    'grey86': RGBColor(219, 219, 219),
    'grey87': RGBColor(222, 222, 222),
    'grey88': RGBColor(224, 224, 224),
    'grey89': RGBColor(227, 227, 227),
    'grey9': RGBColor(23, 23, 23),
    'grey90': RGBColor(229, 229, 229),
    'grey91': RGBColor(232, 232, 232),
    'grey92': RGBColor(235, 235, 235),
    'grey93': RGBColor(237, 237, 237),
    'grey94': RGBColor(240, 240, 240),
    'grey95': RGBColor(242, 242, 242),
    'grey96': RGBColor(245, 245, 245),
    'grey97': RGBColor(247, 247, 247),
    'grey98': RGBColor(250, 250, 250),
    'grey99': RGBColor(252, 252, 252),
    'honeydew': RGBColor(240, 255, 240),
    'honeydew1': RGBColor(240, 255, 240),
    'honeydew2': RGBColor(224, 238, 224),
    'honeydew3': RGBColor(193, 205, 193),
    'honeydew4': RGBColor(131, 139, 131),
    'hotpink': RGBColor(255, 105, 180),
    'hotpink1': RGBColor(255, 110, 180),
    'hotpink2': RGBColor(238, 106, 167),
    'hotpink3': RGBColor(205, 96, 144),
    'hotpink4': RGBColor(139, 58, 98),
    'indianred': RGBColor(205, 92, 92),
    'indianred1': RGBColor(255, 106, 106),
    'indianred2': RGBColor(238, 99, 99),
    'indianred3': RGBColor(205, 85, 85),
    'indianred4': RGBColor(139, 58, 58),
    'indigo': RGBColor(75, 0, 130),
    'ivory': RGBColor(255, 255, 240),
    'ivory1': RGBColor(255, 255, 240),
    'ivory2': RGBColor(238, 238, 224),
    'ivory3': RGBColor(205, 205, 193),
    'ivory4': RGBColor(139, 139, 131),
    'khaki': RGBColor(240, 230, 140),
    'khaki1': RGBColor(255, 246, 143),
    'khaki2': RGBColor(238, 230, 133),
    'khaki3': RGBColor(205, 198, 115),
    'khaki4': RGBColor(139, 134, 78),
    'lavender': RGBColor(230, 230, 250),
    'lavenderblush': RGBColor(255, 240, 245),
    'lavenderblush1': RGBColor(255, 240, 245),
    'lavenderblush2': RGBColor(238, 224, 229),
    'lavenderblush3': RGBColor(205, 193, 197),
    'lavenderblush4': RGBColor(139, 131, 134),
    'lawngreen': RGBColor(124, 252, 0),
    'lemonchiffon': RGBColor(255, 250, 205),
    'lemonchiffon1': RGBColor(255, 250, 205),
    'lemonchiffon2': RGBColor(238, 233, 191),
    'lemonchiffon3': RGBColor(205, 201, 165),
    'lemonchiffon4': RGBColor(139, 137, 112),
    'lightblue': RGBColor(173, 216, 230),
    'lightblue1': RGBColor(191, 239, 255),
    'lightblue2': RGBColor(178, 223, 238),
    'lightblue3': RGBColor(154, 192, 205),
    'lightblue4': RGBColor(104, 131, 139),
    'lightcoral': RGBColor(240, 128, 128),
    'lightcyan': RGBColor(224, 255, 255),
    'lightcyan1': RGBColor(224, 255, 255),
    'lightcyan2': RGBColor(209, 238, 238),
    'lightcyan3': RGBColor(180, 205, 205),
    'lightcyan4': RGBColor(122, 139, 139),
    'lightgoldenrod': RGBColor(238, 221, 130),
    'lightgoldenrod1': RGBColor(255, 236, 139),
    'lightgoldenrod2': RGBColor(238, 220, 130),
    'lightgoldenrod3': RGBColor(205, 190, 112),
    'lightgoldenrod4': RGBColor(139, 129, 76),
    'lightgoldenrodyellow': RGBColor(250, 250, 210),
    'lightgray': RGBColor(211, 211, 211),
    'lightgreen': RGBColor(144, 238, 144),
    'lightgrey': RGBColor(211, 211, 211),
    'lightpink': RGBColor(255, 182, 193),
    'lightpink1': RGBColor(255, 174, 185),
    'lightpink2': RGBColor(238, 162, 173),
    'lightpink3': RGBColor(205, 140, 149),
    'lightpink4': RGBColor(139, 95, 101),
    'lightsalmon': RGBColor(255, 160, 122),
    'lightsalmon1': RGBColor(255, 160, 122),
    'lightsalmon2': RGBColor(238, 149, 114),
    'lightsalmon3': RGBColor(205, 129, 98),
    'lightsalmon4': RGBColor(139, 87, 66),
    'lightseagreen': RGBColor(32, 178, 170),
    'lightskyblue': RGBColor(135, 206, 250),
    'lightskyblue1': RGBColor(176, 226, 255),
    'lightskyblue2': RGBColor(164, 211, 238),
    'lightskyblue3': RGBColor(141, 182, 205),
    'lightskyblue4': RGBColor(96, 123, 139),
    'lightslateblue': RGBColor(132, 112, 255),
    'lightslategray': RGBColor(119, 136, 153),
    'lightslategrey': RGBColor(119, 136, 153),
    'lightsteelblue': RGBColor(176, 196, 222),
    'lightsteelblue1': RGBColor(202, 225, 255),
    'lightsteelblue2': RGBColor(188, 210, 238),
    'lightsteelblue3': RGBColor(162, 181, 205),
    'lightsteelblue4': RGBColor(110, 123, 139),
    'lightyellow': RGBColor(255, 255, 224),
    'lightyellow1': RGBColor(255, 255, 224),
    'lightyellow2': RGBColor(238, 238, 209),
    'lightyellow3': RGBColor(205, 205, 180),
    'lightyellow4': RGBColor(139, 139, 122),
    'lime': RGBColor(0, 255, 0),
    'limegreen': RGBColor(50, 205, 50),
    'linen': RGBColor(250, 240, 230),
    'magenta': RGBColor(255, 0, 255),
    'magenta1': RGBColor(255, 0, 255),
    'magenta2': RGBColor(238, 0, 238),
    'magenta3': RGBColor(205, 0, 205),
    'magenta4': RGBColor(139, 0, 139),
    'maroon': RGBColor(176, 48, 96),
    'maroon1': RGBColor(255, 52, 179),
    'maroon2': RGBColor(238, 48, 167),
    'maroon3': RGBColor(205, 41, 144),
    'maroon4': RGBColor(139, 28, 98),
    'mediumaquamarine': RGBColor(102, 205, 170),
    'mediumblue': RGBColor(0, 0, 205),
    'mediumorchid': RGBColor(186, 85, 211),
    'mediumorchid1': RGBColor(224, 102, 255),
    'mediumorchid2': RGBColor(209, 95, 238),
    'mediumorchid3': RGBColor(180, 82, 205),
    'mediumorchid4': RGBColor(122, 55, 139),
    'mediumpurple': RGBColor(147, 112, 219),
    'mediumpurple1': RGBColor(171, 130, 255),
    'mediumpurple2': RGBColor(159, 121, 238),
    'mediumpurple3': RGBColor(137, 104, 205),
    'mediumpurple4': RGBColor(93, 71, 139),
    'mediumseagreen': RGBColor(60, 179, 113),
    'mediumslateblue': RGBColor(123, 104, 238),
    'mediumspringgreen': RGBColor(0, 250, 154),
    'mediumturquoise': RGBColor(72, 209, 204),
    'mediumvioletred': RGBColor(199, 21, 133),
    'midnightblue': RGBColor(25, 25, 112),
    'mintcream': RGBColor(245, 255, 250),
    'mistyrose': RGBColor(255, 228, 225),
    'mistyrose1': RGBColor(255, 228, 225),
    'mistyrose2': RGBColor(238, 213, 210),
    'mistyrose3': RGBColor(205, 183, 181),
    'mistyrose4': RGBColor(139, 125, 123),
    'moccasin': RGBColor(255, 228, 181),
    'navajowhite': RGBColor(255, 222, 173),
    'navajowhite1': RGBColor(255, 222, 173),
    'navajowhite2': RGBColor(238, 207, 161),
    'navajowhite3': RGBColor(205, 179, 139),
    'navajowhite4': RGBColor(139, 121, 94),
    'navy': RGBColor(0, 0, 128),
    'navyblue': RGBColor(0, 0, 128),
    'oldlace': RGBColor(253, 245, 230),
    'olive': RGBColor(128, 128, 0),
    'olivedrab': RGBColor(107, 142, 35),
    'olivedrab1': RGBColor(192, 255, 62),
    'olivedrab2': RGBColor(179, 238, 58),
    'olivedrab3': RGBColor(154, 205, 50),
    'olivedrab4': RGBColor(105, 139, 34),
    'orange': RGBColor(255, 165, 0),
    'orange1': RGBColor(255, 165, 0),
    'orange2': RGBColor(238, 154, 0),
    'orange3': RGBColor(205, 133, 0),
    'orange4': RGBColor(139, 90, 0),
    'orangered': RGBColor(255, 69, 0),
    'orangered1': RGBColor(255, 69, 0),
    'orangered2': RGBColor(238, 64, 0),
    'orangered3': RGBColor(205, 55, 0),
    'orangered4': RGBColor(139, 37, 0),
    'orchid': RGBColor(218, 112, 214),
    'orchid1': RGBColor(255, 131, 250),
    'orchid2': RGBColor(238, 122, 233),
    'orchid3': RGBColor(205, 105, 201),
    'orchid4': RGBColor(139, 71, 137),
    'palegoldenrod': RGBColor(238, 232, 170),
    'palegreen': RGBColor(152, 251, 152),
    'palegreen1': RGBColor(154, 255, 154),
    'palegreen2': RGBColor(144, 238, 144),
    'palegreen3': RGBColor(124, 205, 124),
    'palegreen4': RGBColor(84, 139, 84),
    'paleturquoise': RGBColor(175, 238, 238),
    'paleturquoise1': RGBColor(187, 255, 255),
    'paleturquoise2': RGBColor(174, 238, 238),
    'paleturquoise3': RGBColor(150, 205, 205),
    'paleturquoise4': RGBColor(102, 139, 139),
    'palevioletred': RGBColor(219, 112, 147),
    'palevioletred1': RGBColor(255, 130, 171),
    'palevioletred2': RGBColor(238, 121, 159),
    'palevioletred3': RGBColor(205, 104, 137),
    'palevioletred4': RGBColor(139, 71, 93),
    'papayawhip': RGBColor(255, 239, 213),
    'peachpuff': RGBColor(255, 218, 185),
    'peachpuff1': RGBColor(255, 218, 185),
    'peachpuff2': RGBColor(238, 203, 173),
    'peachpuff3': RGBColor(205, 175, 149),
    'peachpuff4': RGBColor(139, 119, 101),
    'peru': RGBColor(205, 133, 63),
    'pink': RGBColor(255, 192, 203),
    'pink1': RGBColor(255, 181, 197),
    'pink2': RGBColor(238, 169, 184),
    'pink3': RGBColor(205, 145, 158),
    'pink4': RGBColor(139, 99, 108),
    'plum': RGBColor(221, 160, 221),
    'plum1': RGBColor(255, 187, 255),
    'plum2': RGBColor(238, 174, 238),
    'plum3': RGBColor(205, 150, 205),
    'plum4': RGBColor(139, 102, 139),
    'powderblue': RGBColor(176, 224, 230),
    'purple': RGBColor(160, 32, 240),
    'purple1': RGBColor(155, 48, 255),
    'purple2': RGBColor(145, 44, 238),
    'purple3': RGBColor(125, 38, 205),
    'purple4': RGBColor(85, 26, 139),
    'rebeccapurple': RGBColor(102, 51, 153),
    'red': RGBColor(255, 0, 0),
    'red1': RGBColor(255, 0, 0),
    'red2': RGBColor(238, 0, 0),
    'red3': RGBColor(205, 0, 0),
    'red4': RGBColor(139, 0, 0),
    'rosybrown': RGBColor(188, 143, 143),
    'rosybrown1': RGBColor(255, 193, 193),
    'rosybrown2': RGBColor(238, 180, 180),
    'rosybrown3': RGBColor(205, 155, 155),
    'rosybrown4': RGBColor(139, 105, 105),
    'royalblue': RGBColor(65, 105, 225),
    'royalblue1': RGBColor(72, 118, 255),
    'royalblue2': RGBColor(67, 110, 238),
    'royalblue3': RGBColor(58, 95, 205),
    'royalblue4': RGBColor(39, 64, 139),
    'saddlebrown': RGBColor(139, 69, 19),
    'salmon': RGBColor(250, 128, 114),
    'salmon1': RGBColor(255, 140, 105),
    'salmon2': RGBColor(238, 130, 98),
    'salmon3': RGBColor(205, 112, 84),
    'salmon4': RGBColor(139, 76, 57),
    'sandybrown': RGBColor(244, 164, 96),
    'seagreen': RGBColor(46, 139, 87),
    'seagreen1': RGBColor(84, 255, 159),
    'seagreen2': RGBColor(78, 238, 148),
    'seagreen3': RGBColor(67, 205, 128),
    'seagreen4': RGBColor(46, 139, 87),
    'seashell': RGBColor(255, 245, 238),
    'seashell1': RGBColor(255, 245, 238),
    'seashell2': RGBColor(238, 229, 222),
    'seashell3': RGBColor(205, 197, 191),
    'seashell4': RGBColor(139, 134, 130),
    'sienna': RGBColor(160, 82, 45),
    'sienna1': RGBColor(255, 130, 71),
    'sienna2': RGBColor(238, 121, 66),
    'sienna3': RGBColor(205, 104, 57),
    'sienna4': RGBColor(139, 71, 38),
    'silver': RGBColor(192, 192, 192),
    'skyblue': RGBColor(135, 206, 235),
    'skyblue1': RGBColor(135, 206, 255),
    'skyblue2': RGBColor(126, 192, 238),
    'skyblue3': RGBColor(108, 166, 205),
    'skyblue4': RGBColor(74, 112, 139),
    'slateblue': RGBColor(106, 90, 205),
    'slateblue1': RGBColor(131, 111, 255),
    'slateblue2': RGBColor(122, 103, 238),
    'slateblue3': RGBColor(105, 89, 205),
    'slateblue4': RGBColor(71, 60, 139),
    'slategray': RGBColor(112, 128, 144),
    'slategray1': RGBColor(198, 226, 255),
    'slategray2': RGBColor(185, 211, 238),
    'slategray3': RGBColor(159, 182, 205),
    'slategray4': RGBColor(108, 123, 139),
    'slategrey': RGBColor(112, 128, 144),
    'snow': RGBColor(255, 250, 250),
    'snow1': RGBColor(255, 250, 250),
    'snow2': RGBColor(238, 233, 233),
    'snow3': RGBColor(205, 201, 201),
    'snow4': RGBColor(139, 137, 137),
    'springgreen': RGBColor(0, 255, 127),
    'springgreen1': RGBColor(0, 255, 127),
    'springgreen2': RGBColor(0, 238, 118),
    'springgreen3': RGBColor(0, 205, 102),
    'springgreen4': RGBColor(0, 139, 69),
    'steelblue': RGBColor(70, 130, 180),
    'steelblue1': RGBColor(99, 184, 255),
    'steelblue2': RGBColor(92, 172, 238),
    'steelblue3': RGBColor(79, 148, 205),
    'steelblue4': RGBColor(54, 100, 139),
    'tan': RGBColor(210, 180, 140),
    'tan1': RGBColor(255, 165, 79),
    'tan2': RGBColor(238, 154, 73),
    'tan3': RGBColor(205, 133, 63),
    'tan4': RGBColor(139, 90, 43),
    'teal': RGBColor(0, 128, 128),
    'thistle': RGBColor(216, 191, 216),
    'thistle1': RGBColor(255, 225, 255),
    'thistle2': RGBColor(238, 210, 238),
    'thistle3': RGBColor(205, 181, 205),
    'thistle4': RGBColor(139, 123, 139),
    'tomato': RGBColor(255, 99, 71),
    'tomato1': RGBColor(255, 99, 71),
    'tomato2': RGBColor(238, 92, 66),
    'tomato3': RGBColor(205, 79, 57),
    'tomato4': RGBColor(139, 54, 38),
    'turquoise': RGBColor(64, 224, 208),
    'turquoise1': RGBColor(0, 245, 255),
    'turquoise2': RGBColor(0, 229, 238),
    'turquoise3': RGBColor(0, 197, 205),
    'turquoise4': RGBColor(0, 134, 139),
    'violet': RGBColor(238, 130, 238),
    'violetred': RGBColor(208, 32, 144),
    'violetred1': RGBColor(255, 62, 150),
    'violetred2': RGBColor(238, 58, 140),
    'violetred3': RGBColor(205, 50, 120),
    'violetred4': RGBColor(139, 34, 82),
    'webgray': RGBColor(128, 128, 128),
    'webgreen': RGBColor(0, 128, 0),
    'webgrey': RGBColor(128, 128, 128),
    'webmaroon': RGBColor(128, 0, 0),
    'webpurple': RGBColor(128, 0, 128),
    'wheat': RGBColor(245, 222, 179),
    'wheat1': RGBColor(255, 231, 186),
    'wheat2': RGBColor(238, 216, 174),
    'wheat3': RGBColor(205, 186, 150),
    'wheat4': RGBColor(139, 126, 102),
    'white': RGBColor(255, 255, 255),
    'whitesmoke': RGBColor(245, 245, 245),
    'x11gray': RGBColor(190, 190, 190),
    'x11green': RGBColor(0, 255, 0),
    'x11grey': RGBColor(190, 190, 190),
    'x11maroon': RGBColor(176, 48, 96),
    'x11purple': RGBColor(160, 32, 240),
    'yellow': RGBColor(255, 255, 0),
    'yellow1': RGBColor(255, 255, 0),
    'yellow2': RGBColor(238, 238, 0),
    'yellow3': RGBColor(205, 205, 0),
    'yellow4': RGBColor(139, 139, 0),
    'yellowgreen': RGBColor(154, 205, 50)
}

#: Curses color indices of 8, 16, and 256-color terminals
RGB_256TABLE = (
    RGBColor(0, 0, 0),
    RGBColor(205, 0, 0),
    RGBColor(0, 205, 0),
    RGBColor(205, 205, 0),
    RGBColor(0, 0, 238),
    RGBColor(205, 0, 205),
    RGBColor(0, 205, 205),
    RGBColor(229, 229, 229),
    RGBColor(127, 127, 127),
    RGBColor(255, 0, 0),
    RGBColor(0, 255, 0),
    RGBColor(255, 255, 0),
    RGBColor(92, 92, 255),
    RGBColor(255, 0, 255),
    RGBColor(0, 255, 255),
    RGBColor(255, 255, 255),
    RGBColor(0, 0, 0),
    RGBColor(0, 0, 95),
    RGBColor(0, 0, 135),
    RGBColor(0, 0, 175),
    RGBColor(0, 0, 215),
    RGBColor(0, 0, 255),
    RGBColor(0, 95, 0),
    RGBColor(0, 95, 95),
    RGBColor(0, 95, 135),
    RGBColor(0, 95, 175),
    RGBColor(0, 95, 215),
    RGBColor(0, 95, 255),
    RGBColor(0, 135, 0),
    RGBColor(0, 135, 95),
    RGBColor(0, 135, 135),
    RGBColor(0, 135, 175),
    RGBColor(0, 135, 215),
    RGBColor(0, 135, 255),
    RGBColor(0, 175, 0),
    RGBColor(0, 175, 95),
    RGBColor(0, 175, 135),
    RGBColor(0, 175, 175),
    RGBColor(0, 175, 215),
    RGBColor(0, 175, 255),
    RGBColor(0, 215, 0),
    RGBColor(0, 215, 95),
    RGBColor(0, 215, 135),
    RGBColor(0, 215, 175),
    RGBColor(0, 215, 215),
    RGBColor(0, 215, 255),
    RGBColor(0, 255, 0),
    RGBColor(0, 255, 95),
    RGBColor(0, 255, 135),
    RGBColor(0, 255, 175),
    RGBColor(0, 255, 215),
    RGBColor(0, 255, 255),
    RGBColor(95, 0, 0),
    RGBColor(95, 0, 95),
    RGBColor(95, 0, 135),
    RGBColor(95, 0, 175),
    RGBColor(95, 0, 215),
    RGBColor(95, 0, 255),
    RGBColor(95, 95, 0),
    RGBColor(95, 95, 95),
    RGBColor(95, 95, 135),
    RGBColor(95, 95, 175),
    RGBColor(95, 95, 215),
    RGBColor(95, 95, 255),
    RGBColor(95, 135, 0),
    RGBColor(95, 135, 95),
    RGBColor(95, 135, 135),
    RGBColor(95, 135, 175),
    RGBColor(95, 135, 215),
    RGBColor(95, 135, 255),
    RGBColor(95, 175, 0),
    RGBColor(95, 175, 95),
    RGBColor(95, 175, 135),
    RGBColor(95, 175, 175),
    RGBColor(95, 175, 215),
    RGBColor(95, 175, 255),
    RGBColor(95, 215, 0),
    RGBColor(95, 215, 95),
    RGBColor(95, 215, 135),
    RGBColor(95, 215, 175),
    RGBColor(95, 215, 215),
    RGBColor(95, 215, 255),
    RGBColor(95, 255, 0),
    RGBColor(95, 255, 95),
    RGBColor(95, 255, 135),
    RGBColor(95, 255, 175),
    RGBColor(95, 255, 215),
    RGBColor(95, 255, 255),
    RGBColor(135, 0, 0),
    RGBColor(135, 0, 95),
    RGBColor(135, 0, 135),
    RGBColor(135, 0, 175),
    RGBColor(135, 0, 215),
    RGBColor(135, 0, 255),
    RGBColor(135, 95, 0),
    RGBColor(135, 95, 95),
    RGBColor(135, 95, 135),
    RGBColor(135, 95, 175),
    RGBColor(135, 95, 215),
    RGBColor(135, 95, 255),
    RGBColor(135, 135, 0),
    RGBColor(135, 135, 95),
    RGBColor(135, 135, 135),
    RGBColor(135, 135, 175),
    RGBColor(135, 135, 215),
    RGBColor(135, 135, 255),
    RGBColor(135, 175, 0),
    RGBColor(135, 175, 95),
    RGBColor(135, 175, 135),
    RGBColor(135, 175, 175),
    RGBColor(135, 175, 215),
    RGBColor(135, 175, 255),
    RGBColor(135, 215, 0),
    RGBColor(135, 215, 95),
    RGBColor(135, 215, 135),
    RGBColor(135, 215, 175),
    RGBColor(135, 215, 215),
    RGBColor(135, 215, 255),
    RGBColor(135, 255, 0),
    RGBColor(135, 255, 95),
    RGBColor(135, 255, 135),
    RGBColor(135, 255, 175),
    RGBColor(135, 255, 215),
    RGBColor(135, 255, 255),
    RGBColor(175, 0, 0),
    RGBColor(175, 0, 95),
    RGBColor(175, 0, 135),
    RGBColor(175, 0, 175),
    RGBColor(175, 0, 215),
    RGBColor(175, 0, 255),
    RGBColor(175, 95, 0),
    RGBColor(175, 95, 95),
    RGBColor(175, 95, 135),
    RGBColor(175, 95, 175),
    RGBColor(175, 95, 215),
    RGBColor(175, 95, 255),
    RGBColor(175, 135, 0),
    RGBColor(175, 135, 95),
    RGBColor(175, 135, 135),
    RGBColor(175, 135, 175),
    RGBColor(175, 135, 215),
    RGBColor(175, 135, 255),
    RGBColor(175, 175, 0),
    RGBColor(175, 175, 95),
    RGBColor(175, 175, 135),
    RGBColor(175, 175, 175),
    RGBColor(175, 175, 215),
    RGBColor(175, 175, 255),
    RGBColor(175, 215, 0),
    RGBColor(175, 215, 95),
    RGBColor(175, 215, 135),
    RGBColor(175, 215, 175),
    RGBColor(175, 215, 215),
    RGBColor(175, 215, 255),
    RGBColor(175, 255, 0),
    RGBColor(175, 255, 95),
    RGBColor(175, 255, 135),
    RGBColor(175, 255, 175),
    RGBColor(175, 255, 215),
    RGBColor(175, 255, 255),
    RGBColor(215, 0, 0),
    RGBColor(215, 0, 95),
    RGBColor(215, 0, 135),
    RGBColor(215, 0, 175),
    RGBColor(215, 0, 215),
    RGBColor(215, 0, 255),
    RGBColor(215, 95, 0),
    RGBColor(215, 95, 95),
    RGBColor(215, 95, 135),
    RGBColor(215, 95, 175),
    RGBColor(215, 95, 215),
    RGBColor(215, 95, 255),
    RGBColor(215, 135, 0),
    RGBColor(215, 135, 95),
    RGBColor(215, 135, 135),
    RGBColor(215, 135, 175),
    RGBColor(215, 135, 215),
    RGBColor(215, 135, 255),
    RGBColor(215, 175, 0),
    RGBColor(215, 175, 95),
    RGBColor(215, 175, 135),
    RGBColor(215, 175, 175),
    RGBColor(215, 175, 215),
    RGBColor(215, 175, 255),
    RGBColor(215, 215, 0),
    RGBColor(215, 215, 95),
    RGBColor(215, 215, 135),
    RGBColor(215, 215, 175),
    RGBColor(215, 215, 215),
    RGBColor(215, 215, 255),
    RGBColor(215, 255, 0),
    RGBColor(215, 255, 95),
    RGBColor(215, 255, 135),
    RGBColor(215, 255, 175),
    RGBColor(215, 255, 215),
    RGBColor(215, 255, 255),
    RGBColor(255, 0, 0),
    RGBColor(255, 0, 135),
    RGBColor(255, 0, 95),
    RGBColor(255, 0, 175),
    RGBColor(255, 0, 215),
    RGBColor(255, 0, 255),
    RGBColor(255, 95, 0),
    RGBColor(255, 95, 95),
    RGBColor(255, 95, 135),
    RGBColor(255, 95, 175),
    RGBColor(255, 95, 215),
    RGBColor(255, 95, 255),
    RGBColor(255, 135, 0),
    RGBColor(255, 135, 95),
    RGBColor(255, 135, 135),
    RGBColor(255, 135, 175),
    RGBColor(255, 135, 215),
    RGBColor(255, 135, 255),
    RGBColor(255, 175, 0),
    RGBColor(255, 175, 95),
    RGBColor(255, 175, 135),
    RGBColor(255, 175, 175),
    RGBColor(255, 175, 215),
    RGBColor(255, 175, 255),
    RGBColor(255, 215, 0),
    RGBColor(255, 215, 95),
    RGBColor(255, 215, 135),
    RGBColor(255, 215, 175),
    RGBColor(255, 215, 215),
    RGBColor(255, 215, 255),
    RGBColor(255, 255, 0),
    RGBColor(255, 255, 95),
    RGBColor(255, 255, 135),
    RGBColor(255, 255, 175),
    RGBColor(255, 255, 215),
    RGBColor(255, 255, 255),
    RGBColor(8, 8, 8),
    RGBColor(18, 18, 18),
    RGBColor(28, 28, 28),
    RGBColor(38, 38, 38),
    RGBColor(48, 48, 48),
    RGBColor(58, 58, 58),
    RGBColor(68, 68, 68),
    RGBColor(78, 78, 78),
    RGBColor(88, 88, 88),
    RGBColor(98, 98, 98),
    RGBColor(108, 108, 108),
    RGBColor(118, 118, 118),
    RGBColor(128, 128, 128),
    RGBColor(138, 138, 138),
    RGBColor(148, 148, 148),
    RGBColor(158, 158, 158),
    RGBColor(168, 168, 168),
    RGBColor(178, 178, 178),
    RGBColor(188, 188, 188),
    RGBColor(198, 198, 198),
    RGBColor(208, 208, 208),
    RGBColor(218, 218, 218),
    RGBColor(228, 228, 228),
    RGBColor(238, 238, 238),
)
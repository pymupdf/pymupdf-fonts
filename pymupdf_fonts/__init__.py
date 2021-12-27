# Generated file - DO NOT CHANGE
try:
    import lzma
except ImportError:
    raise ValueError("Require lzma package")


def _cascadia():
    from . import CascadiaMono_Regular

    fontbuffer = CascadiaMono_Regular.fontbuffer[:]
    del CascadiaMono_Regular
    return fontbuffer


def _cascadiai():
    from . import CascadiaMono_Italic

    fontbuffer = CascadiaMono_Italic.fontbuffer[:]
    del CascadiaMono_Italic
    return fontbuffer


def _cascadiab():
    from . import CascadiaMono_Bold

    fontbuffer = CascadiaMono_Bold.fontbuffer[:]
    del CascadiaMono_Bold
    return fontbuffer


def _cascadiabi():
    from . import CascadiaMono_BoldItalic

    fontbuffer = CascadiaMono_BoldItalic.fontbuffer[:]
    del CascadiaMono_BoldItalic
    return fontbuffer


def _figbo():
    from . import FiraGO_Bold

    fontbuffer = FiraGO_Bold.fontbuffer[:]
    del FiraGO_Bold
    return fontbuffer


def _figo():
    from . import FiraGO_Regular

    fontbuffer = FiraGO_Regular.fontbuffer[:]
    del FiraGO_Regular
    return fontbuffer


def _figbi():
    from . import FiraGO_BoldItalic

    fontbuffer = FiraGO_BoldItalic.fontbuffer[:]
    del FiraGO_BoldItalic
    return fontbuffer


def _figit():
    from . import FiraGO_Italic

    fontbuffer = FiraGO_Italic.fontbuffer[:]
    del FiraGO_Italic
    return fontbuffer


def _fimbo():
    from . import FiraMono_Bold

    fontbuffer = FiraMono_Bold.fontbuffer[:]
    del FiraMono_Bold
    return fontbuffer


def _fimo():
    from . import FiraMono_Regular

    fontbuffer = FiraMono_Regular.fontbuffer[:]
    del FiraMono_Regular
    return fontbuffer


def _spacembo():
    from . import SpaceMono_Bold

    fontbuffer = SpaceMono_Bold.fontbuffer[:]
    del SpaceMono_Bold
    return fontbuffer


def _spacembi():
    from . import SpaceMono_BoldItalic

    fontbuffer = SpaceMono_BoldItalic.fontbuffer[:]
    del SpaceMono_BoldItalic
    return fontbuffer


def _spacemit():
    from . import SpaceMono_Italic

    fontbuffer = SpaceMono_Italic.fontbuffer[:]
    del SpaceMono_Italic
    return fontbuffer


def _spacemo():
    from . import SpaceMono_Regular

    fontbuffer = SpaceMono_Regular.fontbuffer[:]
    del SpaceMono_Regular
    return fontbuffer


def _math():
    from . import NotoSansMath_Regular

    fontbuffer = NotoSansMath_Regular.fontbuffer[:]
    del NotoSansMath_Regular
    return fontbuffer


def _music():
    from . import NotoMusic_Regular

    fontbuffer = NotoMusic_Regular.fontbuffer[:]
    del NotoMusic_Regular
    return fontbuffer


def _symbol1():
    from . import NotoSansSymbols_Regular

    fontbuffer = NotoSansSymbols_Regular.fontbuffer[:]
    del NotoSansSymbols_Regular
    return fontbuffer


def _symbol2():
    from . import NotoSansSymbols2_Regular

    fontbuffer = NotoSansSymbols2_Regular.fontbuffer[:]
    del NotoSansSymbols2_Regular
    return fontbuffer


def _notosbo():
    from . import NotoSans_Bold

    fontbuffer = NotoSans_Bold.fontbuffer[:]
    del NotoSans_Bold
    return fontbuffer


def _notosbi():
    from . import NotoSans_BoldItalic

    fontbuffer = NotoSans_BoldItalic.fontbuffer[:]
    del NotoSans_BoldItalic
    return fontbuffer


def _notosit():
    from . import NotoSans_Italic

    fontbuffer = NotoSans_Italic.fontbuffer[:]
    del NotoSans_Italic
    return fontbuffer


def _notos():
    from . import NotoSans_Regular

    fontbuffer = NotoSans_Regular.fontbuffer[:]
    del NotoSans_Regular
    return fontbuffer


def _ubuntu():
    from . import Ubuntu_Regular

    fontbuffer = Ubuntu_Regular.fontbuffer[:]
    del Ubuntu_Regular
    return fontbuffer


def _ubuntubo():
    from . import Ubuntu_Bold

    fontbuffer = Ubuntu_Bold.fontbuffer[:]
    del Ubuntu_Bold
    return fontbuffer


def _ubuntubi():
    from . import Ubuntu_BoldItalic

    fontbuffer = Ubuntu_BoldItalic.fontbuffer[:]
    del Ubuntu_BoldItalic
    return fontbuffer


def _ubuntuit():
    from . import Ubuntu_Italic

    fontbuffer = Ubuntu_Italic.fontbuffer[:]
    del Ubuntu_Italic
    return fontbuffer


def _ubuntm():
    from . import UbuntuMono_Regular

    fontbuffer = UbuntuMono_Regular.fontbuffer[:]
    del UbuntuMono_Regular
    return fontbuffer


def _ubuntmbo():
    from . import UbuntuMono_Bold

    fontbuffer = UbuntuMono_Bold.fontbuffer[:]
    del UbuntuMono_Bold
    return fontbuffer


def _ubuntmbi():
    from . import UbuntuMono_BoldItalic

    fontbuffer = UbuntuMono_BoldItalic.fontbuffer[:]
    del UbuntuMono_BoldItalic
    return fontbuffer


def _ubuntmit():
    from . import UbuntuMono_Italic

    fontbuffer = UbuntuMono_Italic.fontbuffer[:]
    del UbuntuMono_Italic
    return fontbuffer


fontbuffers = {
    "cascadia": _cascadia,
    "cascadiai": _cascadiai,
    "cascadiab": _cascadiab,
    "cascadiabi": _cascadiabi,
    "figbo": _figbo,
    "figo": _figo,
    "figbi": _figbi,
    "figit": _figit,
    "fimbo": _fimbo,
    "fimo": _fimo,
    "spacembo": _spacembo,
    "spacembi": _spacembi,
    "spacemit": _spacemit,
    "spacemo": _spacemo,
    "math": _math,
    "music": _music,
    "symbol1": _symbol1,
    "symbol2": _symbol2,
    "notosbo": _notosbo,
    "notosbi": _notosbi,
    "notosit": _notosit,
    "notos": _notos,
    "ubuntu": _ubuntu,
    "ubuntubo": _ubuntubo,
    "ubuntubi": _ubuntubi,
    "ubuntuit": _ubuntuit,
    "ubuntm": _ubuntm,
    "ubuntmbo": _ubuntmbo,
    "ubuntmbi": _ubuntmbi,
    "ubuntmit": _ubuntmit,
}


fontdescriptors = {}

fontdescriptors["cascadia"] = {
    "name": "Cascadia Mono Regular",
    "size": 454048,
    "mono": True,
    "bold": False,
    "italic": False,
    "serif": True,
    "glyphs": 3199,
}

fontdescriptors["cascadiai"] = {
    "name": "Cascadia Mono Italic",
    "size": 306008,
    "mono": True,
    "bold": False,
    "italic": True,
    "serif": True,
    "glyphs": 1956,
}

fontdescriptors["cascadiab"] = {
    "name": "Cascadia Mono Bold",
    "size": 459644,
    "mono": True,
    "bold": True,
    "italic": False,
    "serif": True,
    "glyphs": 3199,
}

fontdescriptors["cascadiabi"] = {
    "name": "Cascadia Mono Bold Italic",
    "size": 309036,
    "mono": True,
    "bold": True,
    "italic": True,
    "serif": True,
    "glyphs": 1956,
}

fontdescriptors["figbo"] = {
    "name": "FiraGO Bold",
    "size": 807140,
    "mono": False,
    "bold": True,
    "italic": False,
    "serif": True,
    "glyphs": 4577,
}

fontdescriptors["figo"] = {
    "name": "FiraGO Regular",
    "size": 804888,
    "mono": False,
    "bold": False,
    "italic": False,
    "serif": True,
    "glyphs": 4577,
}

fontdescriptors["figbi"] = {
    "name": "FiraGO Bold Italic",
    "size": 813028,
    "mono": False,
    "bold": True,
    "italic": True,
    "serif": True,
    "glyphs": 4577,
}

fontdescriptors["figit"] = {
    "name": "FiraGO Italic",
    "size": 813116,
    "mono": False,
    "bold": False,
    "italic": True,
    "serif": True,
    "glyphs": 4577,
}

fontdescriptors["fimbo"] = {
    "name": "Fira Mono Bold",
    "size": 129004,
    "mono": True,
    "bold": True,
    "italic": False,
    "serif": True,
    "glyphs": 1485,
}

fontdescriptors["fimo"] = {
    "name": "Fira Mono Regular",
    "size": 125712,
    "mono": True,
    "bold": False,
    "italic": False,
    "serif": True,
    "glyphs": 1485,
}

fontdescriptors["spacembo"] = {
    "name": "Space Mono Bold",
    "size": 86740,
    "mono": True,
    "bold": True,
    "italic": False,
    "serif": True,
    "glyphs": 730,
}

fontdescriptors["spacembi"] = {
    "name": "Space Mono Bold Italic",
    "size": 95396,
    "mono": True,
    "bold": True,
    "italic": True,
    "serif": True,
    "glyphs": 730,
}

fontdescriptors["spacemit"] = {
    "name": "Space Mono Italic",
    "size": 103628,
    "mono": True,
    "bold": False,
    "italic": True,
    "serif": True,
    "glyphs": 730,
}

fontdescriptors["spacemo"] = {
    "name": "Space Mono Regular",
    "size": 90972,
    "mono": True,
    "bold": False,
    "italic": False,
    "serif": True,
    "glyphs": 730,
}

fontdescriptors["math"] = {
    "name": "Noto Sans Math Regular",
    "size": 258796,
    "mono": False,
    "bold": False,
    "italic": False,
    "serif": True,
    "glyphs": 2655,
}

fontdescriptors["music"] = {
    "name": "Noto Music Regular",
    "size": 60812,
    "mono": False,
    "bold": False,
    "italic": False,
    "serif": True,
    "glyphs": 579,
}

fontdescriptors["symbol1"] = {
    "name": "Noto Sans Symbols Regular",
    "size": 109696,
    "mono": False,
    "bold": False,
    "italic": False,
    "serif": True,
    "glyphs": 1156,
}

fontdescriptors["symbol2"] = {
    "name": "Noto Sans Symbols2 Regular",
    "size": 375388,
    "mono": False,
    "bold": False,
    "italic": False,
    "serif": True,
    "glyphs": 2674,
}

fontdescriptors["notosbo"] = {
    "name": "Noto Sans Bold",
    "size": 455164,
    "mono": False,
    "bold": True,
    "italic": False,
    "serif": True,
    "glyphs": 3246,
}

fontdescriptors["notosbi"] = {
    "name": "Noto Sans Bold Italic",
    "size": 471004,
    "mono": False,
    "bold": True,
    "italic": True,
    "serif": True,
    "glyphs": 3249,
}

fontdescriptors["notosit"] = {
    "name": "Noto Sans Italic",
    "size": 470472,
    "mono": False,
    "bold": False,
    "italic": True,
    "serif": True,
    "glyphs": 3249,
}

fontdescriptors["notos"] = {
    "name": "Noto Sans Regular",
    "size": 455188,
    "mono": False,
    "bold": False,
    "italic": False,
    "serif": True,
    "glyphs": 3246,
}

fontdescriptors["ubuntu"] = {
    "name": "Ubuntu Regular",
    "size": 298928,
    "mono": False,
    "bold": False,
    "italic": False,
    "serif": True,
    "glyphs": 1262,
}

fontdescriptors["ubuntubo"] = {
    "name": "Ubuntu Bold",
    "size": 269584,
    "mono": False,
    "bold": True,
    "italic": False,
    "serif": True,
    "glyphs": 1262,
}

fontdescriptors["ubuntubi"] = {
    "name": "Ubuntu Bold Italic",
    "size": 282700,
    "mono": False,
    "bold": True,
    "italic": True,
    "serif": True,
    "glyphs": 1266,
}

fontdescriptors["ubuntuit"] = {
    "name": "Ubuntu Italic",
    "size": 326292,
    "mono": False,
    "bold": False,
    "italic": True,
    "serif": True,
    "glyphs": 1266,
}

fontdescriptors["ubuntm"] = {
    "name": "Ubuntu Mono Regular",
    "size": 189004,
    "mono": True,
    "bold": False,
    "italic": False,
    "serif": True,
    "glyphs": 1289,
}

fontdescriptors["ubuntmbo"] = {
    "name": "Ubuntu Mono Bold",
    "size": 174008,
    "mono": True,
    "bold": True,
    "italic": False,
    "serif": True,
    "glyphs": 1286,
}

fontdescriptors["ubuntmbi"] = {
    "name": "Ubuntu Mono Bold Italic",
    "size": 198228,
    "mono": True,
    "bold": True,
    "italic": True,
    "serif": True,
    "glyphs": 1290,
}

fontdescriptors["ubuntmit"] = {
    "name": "Ubuntu Mono Italic",
    "size": 193384,
    "mono": True,
    "bold": False,
    "italic": True,
    "serif": True,
    "glyphs": 1293,
}


def myfont(name):
    name = name.lower()
    if name not in fontbuffers.keys():
        msg = "Unknown fontname: " + name
        raise ValueError(msg)
    return fontbuffers[name]()


def fitzfont(name):
    try:
        import fitz
    except ImportError:
        raise ImportError("Install PyMuPDF to use this method.")
    return fitz.Font(fontbuffer=myfont(name))

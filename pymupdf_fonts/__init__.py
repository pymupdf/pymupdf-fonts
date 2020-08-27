# Generated file - DO NOT CHANGE
try:
    import lzma
except ImportError:
    raise ValueError("Require lzma package")


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


fontbuffers = {
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
}


fontdescriptors = {}

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
    "size": 251968,
    "mono": False,
    "bold": False,
    "italic": False,
    "serif": True,
    "glyphs": 2655,
}

fontdescriptors["music"] = {
    "name": "Noto Music Regular",
    "size": 60824,
    "mono": False,
    "bold": False,
    "italic": False,
    "serif": True,
    "glyphs": 579,
}

fontdescriptors["symbol1"] = {
    "name": "Noto Sans Symbols Regular",
    "size": 107580,
    "mono": False,
    "bold": False,
    "italic": False,
    "serif": True,
    "glyphs": 1154,
}

fontdescriptors["symbol2"] = {
    "name": "Noto Sans Symbols2 Regular",
    "size": 318416,
    "mono": False,
    "bold": False,
    "italic": False,
    "serif": True,
    "glyphs": 2277,
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

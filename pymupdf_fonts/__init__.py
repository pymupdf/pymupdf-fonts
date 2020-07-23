try:
    import lzma
except ImportError:
    raise ValueError("Require lzma package")


def _figo():
    from . import FiraGO_Regular

    return FiraGO_Regular.fontbuffer


def _figbo():
    from . import FiraGO_Bold

    return FiraGO_Bold.fontbuffer


def _figit():
    from . import FiraGO_Italic

    return FiraGO_Italic.fontbuffer


def _figbi():
    from . import FiraGO_BoldItalic

    return FiraGO_BoldItalic.fontbuffer


def _fimo():
    from . import FiraMono_Regular

    return FiraMono_Regular.fontbuffer


def _fimbo():
    from . import FiraMono_Bold

    return FiraMono_Bold.fontbuffer


fontbuffers = {
    "figo": _figo,
    "figbo": _figbo,
    "figit": _figit,
    "figbi": _figbi,
    "fimo": _fimo,
    "fimbo": _fimbo,
}


def myfont(name):
    name = name.lower()
    if name not in fontbuffers.keys():
        msg = "Unknown fontname: " + name
        raise ValueError(msg)
    return fontbuffers[name]()


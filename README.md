# pymupdf-fonts
Collection of optional fonts for PyMuPDF

Release date: July 31, 2020

# Author

* Jorj X. McKie

# Introduction

This is a collection of fonts that can be used by PyMuPDF applications for writing text to PDFs.

The fonts are provided encoded in compressed base64 format, wrapped as Python variables.

The primary motivation for this approach is two-fold:

1. keep the PyMuPDF binary module size within reasonable limits by not adding more fonts to it, and
2. enable the inclusion of arbitrary fonts that are not contained in the MuPDF library. We also may extend this repository with selected Google's NOTO fonts.

Currently the following fonts are provided:
* **FiraGO** font family made by Mozilla.org. These are sans serif **proportional** fonts with support for 68 languages and the following scripts: Latin, Cyrillic, Greek, Arabic, Hebrew, Thai, Georgian and Devanagari. Support for the variants **Regular**, **Bold**, **Ialic** and **Bold-Italic**. If you do not need Asian script support (CJK), use it as a viable "universal" alternative to the **"Droid Sans Fallback Regular"** font (which is part of PyMuPDF's binary).
* **FiraMono** font family made by Mozilla.org, sans serif **mono-spaced** fonts with support for dozens of languages and the scripts Latin, Cyrillic, Greek. Supports the weights **Regular** and **Bold**, but no italics. Can be used instead of Courier for a nicer look.
* **Space Mono** (my personal favorite) a nice and small-sized **mono-spaced** font family. It is an original fixed-width type family designed by Colophon Foundry for Google Design. It supports a Latin Extended glyph set, enables typesetting for English and other Western European languages. Part of Google Fonts and also licensed by the [Open Font License](https://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL). Supports **Regular**, **Bold*, **Italic** and **Bold-Italic**. Can be used instead of Courier for a nicer look.
* **Noto Sans Math Regular** a NOTO font from Google providing mathematical symbols.
* **Noto Music Regular** a NOTO font from Google providing musical symbols.
* **Noto Sans Symbols Regular** a Google NOTO replacement for the Base-14 Symbol font.
* **Noto Sans Symbols2 Regular** an extension for the previous.
* **Noto Sans** a Google NOTO font family replacement for Helvetica / Arial, which support all four weights regular, bold, italics and bold-italics.


# Installation

pymupdf_fonts is a pure Python package provided as a wheel. As such it is Python version independent. The fonts provided here are lzma-compressed. This is a standard module in Python 3, but not in Python 2. Therefore, there is **no support for Python 2**.

# Usage and Documentation

If the package is installed, PyMuPDF supports the fonts automatically. To use one, execute ``font = fitz.Font("code")``, where ``code`` is a value from the first table column below.

You can then either use the ``font`` object directly in PyMuPDF's ``TextWriter`` class, or use its buffer in the conventional `Page.insertFont()` / `Page.insertText()` / `Page.insertTextbox()` methods like this:

```python
xref = page.insertFont(fontname="F0", fontbuffer=font.buffer)
```

For more detail consult the PyMuPDF documentation of the [Font](https://pymupdf.readthedocs.io/en/latest/font.html) class.


| code | font | version | comment |
|------|------|---------|---------|
| figo | FiraGO_Regular | 1.0.0 |
| figbo | FiraGO_Bold | 1.0.0 |
| figit | FiraGO_Italic | 1.0.0 |
| figbi | FiraGO_BoldItalic | 1.0.0 |
| fimo | FiraMono_Regular | 1.0.0 |
| fimbo | FiraMono_Bold | 1.0.0 |
| spacemo | SpaceMono_Regular | 1.0.1 | mono-spaced
| spacembo | SpaceMono_Bold | 1.0.1 | mono bold
| spacemit | SpaceMono_Italic | 1.0.1 | mono italic
| spacembi | SpaceMono_BoldItalic | 1.0.1 | mono bold-italic
| math | Noto Sans Math Regular | 1.0.2 | math symbols |
| music | Noto Music Regular | 1.0.2 | musical symbols |
| symbol1 | Noto Sans Symbols Regular | 1.0.2 | replaces "symb" |
| symbol2 | Noto Sans Symbols2 Regular | 1.0.2 | extended symbols |
| notos | Noto Sans Regular | 1.0.3 | similar to Arial |
| notosbi | Noto Sans Italic | 1.0.3 | 
| notosbo | Noto Sans Bold | 1.0.3 |
| notosbi | Noto Sans Bold Italic | 1.0.3 |

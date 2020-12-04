# pymupdf-fonts
Collection of optional fonts for PyMuPDF

Release date: July 31, 2020

# Author

* Jorj X. McKie

# Introduction

This is a collection of fonts that can be used by PyMuPDF applications for writing text to PDFs.

The fonts are provided encoded in compressed base64 format, wrapped as Python variables.

The primary motivation for this approach is two-fold: (1) keep the PyMuPDF binary module size within reasonable limits by not adding more fonts to it, and (2) enable the inclusion of arbitrary fonts that are not contained in the MuPDF library. We also may extend this repository with selected Google's NOTO fonts.

When using a certain font, its corresponding Python value is imported, automatically decompressed / decoded and stored as a ``bytes`` object. This value can then be used as a fontbuffer by any PyMuPDF method which needs a font.

Currently the following fonts are provided:
* **FiraGO** font family made by Mozilla.org, sans serif **proportional** fonts with support for 68 languages and the following scripts: Latin, Cyrillic, Greek, Arabic, Hebrew, Thai, Georgian and Devanagari. Support for the variants **Regular**, **Bold**, **Ialic** and **Bold-Italic**. Use this font as a viable "universal" alternative to the **"Droid Sans Fallback Regular"** font, which is included in the PyMuPDF package (embedded in the binary extension module).
* **FiraMono** font family made by Mozilla.org, sans serif **mono-spaced** fonts with support for dozens of languages and the scripts Latin, Cyrillic, Greek. Supports the weights **Regular** and **Bold**, but no italics. Can be used instead of Courier for a nicer look.
* **Space Mono** (new in version 1.0.1), my persoanl favorite, a nice and small-sized **mono-spaced** font family. It is an original fixed-width type family designed by Colophon Foundry for Google Design. It supports a Latin Extended glyph set, enables typesetting for English and other Western European languages. Part of Google Fonts and also licensed by the [Open Font License](https://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL). Supports **Regular**, **Bold*, **Italic** and **Bold-Italic**. Can be used instead of Courier for a nicer look.

# Installation

pymupdf_fonts is a pure Python package provided as a wheel. As such it is Python version independent. The fonts provided here are lzma-compressed. This is a standard module in Python 3, but not in Python 2. Therefore, there is no support for Python 2.

# Usage and Documentation

PyMuPDF supports these fonts rightaway. Using the fonts is documented in detail in PyMuPDF. In short, to create the desired font, execute ``font = fitz.Font("code")`` with one of the values in the ``code`` column below.


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

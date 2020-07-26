# pymupdf-fonts
Collection of optional fonts for PyMuPDF

Release date: July 31, 2020

# Author

* Jorj X. McKie

# Introduction

This is a collection of fonts that can be used by PyMuPDF applications for writing text to PDFs.

The fonts are provided encoded in compressed base64 format, wrapped as Python variables.

The primary motivation for this approach is two-fold: (1) keep the PyMuPDF binary module size within reasonable limits and (2) enable inclusion of fonts not supported by the MuPDF library. We may extend this repository with Google's NOTO fonts.

To use a certain font, its corresponding Python value is imported, which automatically decompresses and decodes the font's binary image into a ``bytes`` object. This value can then be used as a fontbuffer by any PyMuPDF method which needs a font.

Currently the following fonts are provided:
* **FiraGO** font family made by Mozilla.org, sans serif **proportional** fonts with support for 68 languages and the following scripts: Latin, Cyrillic, Greek, Arabic, Hebrew, Thai, Georgian and Devanagari. Support for the variants **Regular**, **Bold**, **Ialic** and **Bold-Italic**. Use this font as a viable "universal" alternative to the **"Droid Sans Fallback Regular"** font, which is included in the PyMuPDF package (embedded in the binary extension module).
* **FiraMono** font family made by Mozilla.org, sans serif **mono-spaced** fonts with support for dozens of languages and the scripts Latin, Cyrillic, Greek. Supports the weights **Regular** and **Bold** (no Italic). Can be used instead of Courier for a nicer look.
* **Space Mono** (new in version 1.0.1) a nice and small-sized **mono-spaced** font family. Space Mono is an original fixed-width type family designed by Colophon Foundry for Google Design. It supports a Latin Extended glyph set, enabling typesetting for English and other Western European languages. Part of Google Fonts and also licensed by the [Open Font License](https://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL). Supports Regular, Bold, Italic and Bild-Italic.

# Installation

pymupdf_fonts is a pure Python package provided as a wheel. As such it is Python version independent. The fonts provided here are lzma-compressed. This is a standard module in Python 3. Therefore, there is no support for Python 2.

# Usage and Documentation

PyMuPDF supports these fonts rightaway. Using the fonts is documented in detail in PyMuPDF. In short, accessing the desired font buffer, do this:

```python
import pymupdf_fonts
fontbuffer = pymupdf_fonts.myfont(code)  # suitable string 'code'
# Then execute page methods insertFont, insertText, insertTextbox
# using the fontbuffer option.
# Similarly when using the TextWriter class.
```

In PyMuPDF v1.17.4 we will simplify the usage by convenience wrappers. E.g. to use font "Fira Mono Regular" just do this: ``font = fitz.Font("fimo")``.

The following table maps `"code"` values to fonts:

| code | font |
|------|------|
| figo | FiraGO_Regular |
| figbo | FiraGO_Bold |
| figit | FiraGO_Italic |
| figbi | FiraGO_BoldItalic |
| fimo | FiraMono_Regular |
| fimbo | FiraMono_Bold |
| spacemo | SpaceMono_Regular |
| spacembo | SpaceMono_Bold |
| spacemit | SpaceMono_Italic |
| spacembi | SpaceMono_BoldItalic |

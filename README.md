# pymupdf-fonts
Collection of optional fonts for PyMuPDF

Release date: December 27, 2021

# Author

* Jorj X. McKie

# Introduction

This is a collection of fonts that can be used by PyMuPDF applications for writing text to PDFs.

The fonts are provided encoded in compressed base64 format, wrapped as Python variables.

The primary motivation for this approach is two-fold:

1. keep the PyMuPDF binary module size within reasonable limits by not adding more fonts to it, and
2. enable the inclusion of arbitrary fonts that are not contained in the MuPDF library. We also may extend this repository with selected fonts.

Currently the following fonts are provided:
* **FiraGO** font family made by Mozilla.org. These are sans-serif **proportional** fonts with support for 68 languages and the following scripts: Latin, Cyrillic, Greek, Arabic, Hebrew, Thai, Georgian and Devanagari. They support the weights **Regular**, **Bold**, **Ialic** and **Bold-Italic**. If you do not need Asian script support (CJK), use it as a viable "universal" alternative to the **"Droid Sans Fallback Regular"** font (which is part of PyMuPDF's binary).
* **FiraMono** font family made by Mozilla.org, sans serif **mono-spaced** fonts with support for dozens of languages and the scripts Latin, Cyrillic, Greek. Supports the weights **Regular** and **Bold**, but no italics. Can be used instead of Courier for a nicer look.
* **Space Mono** (my personal favorite) a nice and small-sized **mono-spaced** font family. It is an original fixed-width type family designed by Colophon Foundry for Google Design. It supports a Latin Extended glyph set, enables typesetting for English and other Western European languages. Part of Google Fonts and also licensed under the [Open Font License](https://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL). Supports **Regular**, **Bold**, **Italic** and **Bold-Italic**. Can be used instead of Courier for a nicer look.
* **Noto Sans Math Regular** a NOTO font from Google providing mathematical symbols.
* **Noto Music Regular** a NOTO font from Google providing musical symbols.
* **Noto Sans Symbols Regular** a Google NOTO replacement for the Base-14 Symbol font.
* **Noto Sans Symbols2 Regular** an extension for the previous.
* **Noto Sans** a Google NOTO font family replacement for Helvetica / Arial, which support all four weights regular, bold, italics and bold-italics.
* **Ubuntu** font families of sans-serif proportional and mono-spaced fonts, that provide a look familiar to Ubuntu users. They are licensed under a slightly different license - see below - which nonetheless offers a similar degree of freedom as the OFL.
* **Cascadia Mono** mono-spaced font family made by Microsoft. Supports **Regular**, **Bold**, **Italic** and **Bold-Italic**. Can be used instead of Courier for a nicer look. License SIL OFL v1.1.


# Installation

pymupdf_fonts is a pure Python package provided as a wheel. As such it is Python version independent and can be installed via `python -m pip install pymupdf-fonts`.

# Usage and Documentation

If the package is installed, PyMuPDF supports all the fonts automatically. To use one of these fonts, simply execute ``font = fitz.Font("code")``, where ``code`` is a value from the first table column below. So this works as if the list of standard font codes ""helv", "tiro", "cour", etc. had been extended by new codes.

You can then either use the ``font`` object directly in PyMuPDF's ``TextWriter`` class, or **use its buffer** in the conventional `Page.insert_font()` / `Page.insert_text()` / `Page.insert_textbox()` methods like this:

```python
page.insert_font(fontname="F0", fontbuffer=font.buffer)
page.insert_text(point, text, fontname="F0", ...)
# or similarly:
page.insert_textbox(rect, text, fontname="F0", ...)
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
| ubuntu | Ubuntu Regular | 1.0.4 | sans-serif, for texts in Ubuntu look
| ubuntubo | Ubuntu Bold | 1.0.4 |
| ubuntubi | Ubuntu Bold Italic | 1.0.4 |
| ubuntuit | Ubuntu Italic | 1.0.4 |
| ubuntm | Ubuntu Mono Regular | 1.0.4 | mono-spaced version of Ubuntu fonts
| ubuntmbo | Ubuntu Mono Bold | 1.0.4 |
| ubuntmbi | Ubuntu Mono Bold Italic | 1.0.4 |
| ubuntmit | Ubuntu Mono Italic | 1.0.4 |
| cascadia | Cascadia Mono Regular | 1.0.5 |
| cascadiab | Cascadia Mono Bold | 1.0.5 |
| cascadiai | Cascadia Mono Italic | 1.0.5 |
| cascadiabi | Cascadia Mono BoldItalic | 1.0.5 |

# License
Most of the fonts above are licensed under the SIL OFL v1.1 license, which is stored as file `LICENSE.txt` in this repository.
The Ubuntu fonts are available under a similar free license, to be found here: [Ubuntu Font License](http://font.ubuntu.com/ufl/).

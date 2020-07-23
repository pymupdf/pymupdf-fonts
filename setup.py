import setuptools

pkg_tab = open("PKG-INFO").read().split("\n")
long_dtab = []
classifier = []
for l in pkg_tab:
    if l.startswith("Classifier: "):
        classifier.append(l[12:])
        continue
    if l.startswith(" "):
        long_dtab.append(l.strip())
long_desc = "\n".join(long_dtab)


setuptools.setup(
    name="pymupdf_fonts",
    version="1.0.0",
    author="Jorj McKie",
    author_email="jorj.x.mckie@outlook.de",
    description="Collection of font binaries for use in PyMuPDF",
    packages=setuptools.find_packages(),
    long_description=long_desc,
    url="https://github.com/pymupdf/pymupdf_fonts",
    classifiers=classifier,
)

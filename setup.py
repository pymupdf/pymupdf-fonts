import setuptools
import os

setup_py_cwd = os.path.dirname(__file__)
with open(os.path.join(setup_py_cwd, "README.md"), encoding="utf-8") as f:
    readme = f.read()

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Classifier: Environment :: Console",
    "Classifier: Intended Audience :: Developers",
    "Classifier: Programming Language :: Python :: 3",
    "Classifier: Topic :: Utilities",
]

setuptools.setup(
    name="pymupdf_fonts",
    version="1.0.5",
    author="Jorj McKie",
    author_email="jorj.x.mckie@outlook.de",
    description="Collection of font binaries for use in PyMuPDF",
    packages=setuptools.find_packages(),
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/pymupdf/pymupdf-fonts",
    classifiers=classifiers,
    project_urls={
        "Documentation": "https://pymupdf.readthedocs.io/en/latest/font.html",
        "Download": "https://github.com/pymupdf/pymupdf-fonts/releases",
    },
    license="SIL OFL V1.1",
)

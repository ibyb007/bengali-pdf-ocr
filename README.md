# Bengali PDF OCR Converter

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/) [![Actions Status](https://github.com/ibyb007/bengali-pdf-ocr/workflows/OCR%20PDF/badge.svg)](https://github.com/ibyb007/bengali-pdf-ocr/actions) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple Python tool to convert scanned (image-based) Bengali PDFs into fully searchable PDFs with selectable text. Uses Tesseract OCR for Bengali language support, preserving the original layout while adding an invisible text layer.

## Features
- **Bengali OCR Support**: Handles Devanagari script via `lang='ben'`.
- **High-Quality Processing**: Configurable DPI for image conversion (default 300).
- **CLI-Friendly**: Easy command-line usage.
- **GitHub Automation**: Optional workflow to process PDFs directly in the repo—no local setup needed.
- **Lightweight**: Relies on battle-tested libraries (pdf2image, pytesseract, PyMuPDF).

## Prerequisites
- **Python 3.8+**.
- **Tesseract OCR** with Bengali language pack:
  - **Ubuntu/Debian**: `sudo apt update && sudo apt install tesseract-ocr tesseract-ocr-ben poppler-utils`
  - **macOS**: `brew install tesseract tesseract-lang poppler`
  - **Windows**: Download installer from [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract/wiki), add to PATH, and install the `ben` (Bengali) language data pack from [traineddata repo](https://github.com/tesseract-ocr/tessdata).
- Verify: Run `tesseract --version` and `tesseract --list-langs` (should include `ben`).

## Installation
1. Clone the repo: ```git clone https://github.com/ibyb007/bengali-pdf-ocr.git cd bengali-pdf-ocr```
2. Install dependencies: ```pip install -r requirements.txt```
3. ## Usage
'''python converter.py input.pdf output.pdf```
### Local Command-Line
Process a PDF file:
- **Optional DPI**: Edit the script's `convert_pdf` function to accept a third arg (e.g., `dpi=400`) for higher accuracy (slower, better for low-res scans).

Example:
- Input: A scanned Bengali document (`scanned.pdf`).
- Output: `searchable.pdf`—open in any PDF viewer (e.g., Adobe Acrobat) and search/select text.

## License
MIT License—feel free to use, modify, and distribute. See [LICENSE](LICENSE) for details.

## Acknowledgments
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for the engine.
- Libraries: [pdf2image](https://github.com/Belval/pdf2image), [pytesseract](https://github.com/madmaze/pytesseract), [PyMuPDF](https://github.com/pymupdf/PyMuPDF).

Questions or issues? Open a GitHub Issue. Star the repo if it helps—let's make Bengali docs searchable! 
### As a Library
```python
from converter import convert_pdf

convert_pdf("input.pdf", "output.pdf", dpi=300)

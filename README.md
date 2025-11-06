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
1. Clone the repo: git clone https://github.com/ibyb007/bengali-pdf-ocr.git cd bengali-pdf-ocr
2. Install dependencies: pip install -r requirements.txt
   ## Usage

### Local Command-Line
Process a PDF file:python converter.py input_scanned.pdf output_searchable.pdf
- **Optional DPI**: Edit the script's `convert_pdf` function to accept a third arg (e.g., `dpi=400`) for higher accuracy (slower, better for low-res scans).

Example:
- Input: A scanned Bengali document (`scanned.pdf`).
- Output: `searchable.pdf`—open in any PDF viewer (e.g., Adobe Acrobat) and search/select text.

### As a Library
```python
from converter import convert_pdf

convert_pdf("input.pdf", "output.pdf", dpi=300)
GitHub-Only Processing (Automated)
For hands-off conversion without local tools:
Upload your scanned PDF to the repo as input.pdf (via Add file > Upload files; keep under 10MB for quick runs).
The .github/workflows/ocr.yml workflow auto-triggers on push:
Installs deps and Tesseract.
Runs python converter.py input.pdf output.pdf.
Commits the searchable output.pdf back to the repo.
Monitor in the Actions tab (runs in ~1-2 minutes on Ubuntu runner).
Download output.pdf from the repo—done!
Note: Free GitHub Actions has limits (2,000 minutes/month); large PDFs may timeout.
Testing
Local:
Grab a sample scanned Bengali PDF (e.g., from public archives like Bangla books).
Run the command above.
Verify: Open output in a viewer, search for a Bengali word (e.g., "বাংলা").
GitHub:
Upload a 1-page test PDF as input.pdf.
Push/commit.
Check Actions for success; refresh repo for output.pdf.
Add a test script in tests/ later if expanding.
Troubleshooting
Tesseract Not Found: Ensure it's in PATH; test with tesseract --version.
Low OCR Accuracy: Increase DPI (400+), use cleaner scans, or preprocess images (e.g., via Pillow for contrast).
PDF Too Large: Split into smaller files; Actions may fail on >50 pages.
Errors:
No module named 'pdf2image': Run pip install -r requirements.txt.
Poppler missing: Install via OS package manager (e.g., sudo apt install poppler-utils).
Logs: For Actions, click the job > "Convert" step.
Contributing
Fork the repo.
Create a branch: git checkout -b feature/your-feature.
Commit: git commit -m "Add your feature".
Push: git push origin feature/your-feature.
Open a Pull Request.
Ideas: Add GUI (Tkinter/Streamlit), multiprocessing for speed, or multi-lang support.
License
MIT License—feel free to use, modify, and distribute. See LICENSE for details.
Acknowledgments
Tesseract OCR for the engine.
Libraries: pdf2image, pytesseract, PyMuPDF.
Questions or issues? Open a GitHub Issue. Star the repo if it helps—let's make Bengali docs searchable! 

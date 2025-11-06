# Bengali PDF OCR Converter

Convert scanned (image-based) Bengali PDFs into fully searchable PDFs with selectable text using Tesseract OCR. Retains original layout while adding an invisible text layer.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features
- Supports Bengali language OCR (`lang='ben'`).
- High-quality image conversion (configurable DPI).
- Outputs searchable PDF with original visuals intact.
- CLI-friendly for batch processing.

## Installation

### Prerequisites
- **Tesseract OCR**: Install with Bengali support.
  - Ubuntu/Debian: `sudo apt install tesseract-ocr tesseract-ocr-ben poppler-utils`
  - macOS: `brew install tesseract tesseract-lang poppler`
  - Windows: Download from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki), add to PATH, and install `tesseract-ocr-ben` language pack.
- Python 3.8+.

### Via pip (Recommended)
1. Clone the repo:
# Bengali PDF OCR Converter

Turns scanned Bengali PDFs into searchable ones.

## Install
- Tesseract OCR (with Bengali): Ubuntu `sudo apt install tesseract-ocr tesseract-ocr-ben poppler-utils`; macOS `brew install tesseract tesseract-lang poppler`; Windows: Download installer + ben lang pack.
- Python deps: `pip install -r requirements.txt`

## Use

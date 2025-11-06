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
1. Clone the repo:

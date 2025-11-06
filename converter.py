import pytesseract
from pdf2image import convert_from_path
import fitz
import sys
import glob
import os

def convert_pdf(input_path, output_path, dpi=300):
    print("Converting PDF to images...")
    images = convert_from_path(input_path, dpi=dpi)

    print("Running OCR...")
    snippets = []
    for i, img in enumerate(images):
        print(f"Page {i+1}")
        # Use both English and Bengali for OCR
        pdf_bytes = pytesseract.image_to_pdf_or_hocr(img, extension='pdf', lang='eng+ben')
        snippets.append(pdf_bytes)

    print("Merging...")
    doc = fitz.open()
    for bytes_pdf in snippets:
        temp = fitz.open("pdf", bytes_pdf)
        doc.insert_pdf(temp)
        temp.close()

    doc.save(output_path)
    doc.close()
    print(f"Done: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        convert_pdf(sys.argv[1], sys.argv[2])
    else:
        pdf_files = glob.glob('*.pdf')
        for pdf_file in pdf_files:
            if os.path.basename(pdf_file).lower() != 'output.pdf':
                output_path = pdf_file.replace('.pdf', '_ocr.pdf')
                convert_pdf(pdf_file, output_path)
        if not pdf_files:
            print("No PDF files found in the current directory.")
        elif all(os.path.basename(f).lower() == 'output.pdf' for f in pdf_files):
            print("Only output.pdf found; no other PDFs to process.")

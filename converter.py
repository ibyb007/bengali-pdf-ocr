import pytesseract
from pdf2image import convert_from_path
import fitz
import sys

def convert_pdf(input_path, output_path, dpi=300):
    print("Converting PDF to images...")
    images = convert_from_path(input_path, dpi=dpi)

    print("Running OCR...")
    snippets = []
    for i, img in enumerate(images):
        print(f"Page {i+1}")
        pdf_bytes = pytesseract.image_to_pdf_or_hocr(img, extension='pdf', lang='ben')
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
    if len(sys.argv) != 3:
        print("Usage: python converter.py input.pdf output.pdf")
        sys.exit(1)
    convert_pdf(sys.argv[1], sys.argv[2])

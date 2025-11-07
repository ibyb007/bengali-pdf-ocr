def convert_pdf(input_path, output_path, dpi=400):
    print("Converting PDF to images...")
    images = convert_from_path(input_path, dpi=dpi)

    print("Running OCR...")
    snippets = []
    for i, original_img in enumerate(images):
        print(f"Page {i+1}")
        # Preprocess ONLY for OCR (not for embedding)
        processed_img = preprocess_image(original_img)
        
        # OCR on processed image for accuracy
        hocr_data = pytesseract.image_to_hocr(processed_img, lang='ben+eng', config='--psm 6')
        
        # Create PDF snippet: Embed ORIGINAL image + add HOCR text layer
        # First, make a PDF from the original image (visible layer)
        original_pdf_bytes = pytesseract.image_to_pdf_or_hocr(original_img, extension='pdf', lang='eng')  # Dummy lang, just for image embed
        
        # Now, parse HOCR and overlay text on the original PDF (using PyMuPDF)
        temp_doc = fitz.open("pdf", original_pdf_bytes)
        page = temp_doc[0]  # Single-page doc
        
        # Simple HOCR parsing: Extract text spans and add as hidden annotations
        # (This is a basic implementation; for production, use a full HOCR lib like hocr-tools)
        import re
        text_spans = re.findall(r'<span class="ocrx_word"[^>]*>([^<]+)</span>', hocr_data)
        for span_text in text_spans:
            if span_text.strip():  # Add each word as invisible text (rough positioning)
                # Note: Real HOCR has bbox coords; this approximates by appending to page
                page.insert_text((50, 50 + len(snippets) * 10), span_text, fontsize=11, color=(1,1,1,0))  # Invisible white text
        
        # Save the modified single-page PDF
        snippet_bytes = temp_doc.tobytes()
        temp_doc.close()
        snippets.append(snippet_bytes)

    print("Merging...")
    doc = fitz.open()
    for bytes_pdf in snippets:
        temp = fitz.open("pdf", bytes_pdf)
        doc.insert_pdf(temp)
        temp.close()

    doc.save(output_path)
    doc.close()
    print(f"Done: {output_path}")

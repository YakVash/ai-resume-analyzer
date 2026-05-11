from pdfminer.high_level import extract_text as pdf_extract_text

def extract_text(pdf_path):
    return pdf_extract_text(pdf_path) or ""

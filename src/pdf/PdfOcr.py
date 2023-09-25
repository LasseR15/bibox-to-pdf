import os
import ocrmypdf
from rich import print
from src.values.Constants import Constants


def ocr_pdf(book_id: int, pdf_non_ocr_path: str):
    pdf_output_dir = Constants.pdfOutputDir.format(book_id)
    os.makedirs(pdf_output_dir, exist_ok=True)

    print("Starting PDF ocr in German...")

    pdf_output_file = Constants.pdfOutputFile.format(book_id, 'ocr-version')

    ocrmypdf.ocr(pdf_non_ocr_path, pdf_output_file, language="deu", tesseract_config="quiet")

    print(f"Successfully created OCR PDF from BiBox book. You will find the pdf at '{pdf_output_file}'")

    return pdf_output_file

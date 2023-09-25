import os
import img2pdf
from rich import print
from src.values.Constants import Constants


def create_pdf_from_images(book_id: int, image_paths: []):
    pdf_output_dir = Constants.pdfOutputDir.format(book_id)
    os.makedirs(pdf_output_dir, exist_ok=True)

    pdf_file_path = Constants.pdfOutputFile.format(book_id, 'non-ocr-version')

    with open(pdf_file_path, "wb") as f:
        f.write(img2pdf.convert(image_paths))

    print(f"Successfully created non-OCR PDF from images. You will find the generated pdf at '{pdf_file_path}'")

    return pdf_file_path

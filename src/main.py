import typer
from typing_extensions import Annotated
from src.bibox.BiboxImageDownloader import get_bibox_images, download_images_from_bibox
from src.bibox.BiboxLogin import login_to_bibox
from src.pdf.PdfCreator import create_pdf_from_images
from src.pdf.PdfOcr import ocr_pdf
from src.values.Constants import Constants
from rich import print


def main(
        username: Annotated[str, typer.Argument()],
        password: Annotated[str, typer.Argument()],
        book_id: Annotated[int, typer.Argument()]):

    book_dest_path = Constants.bookBaseOutputDir.format(book_id)
    print(f"Downloading book with id '{book_id}' to '{book_dest_path}'...")

    access_token = login_to_bibox(username, password)

    bibox_images = get_bibox_images(access_token, book_id)
    image_paths = download_images_from_bibox(bibox_images, book_id)
    pdf_non_ocr_path = create_pdf_from_images(book_id, image_paths)
    ocr_pdf(book_id, pdf_non_ocr_path)


if __name__ == "__main__":
    typer.run(main)

import typer
from typing_extensions import Annotated
from bibox_to_pdf.bibox.BiboxImageDownloader import get_bibox_images, download_images_from_bibox
from bibox_to_pdf.bibox.BiboxLogin import login_to_bibox
from bibox_to_pdf.pdf.PdfCreator import create_pdf_from_images
from bibox_to_pdf.pdf.PdfOcr import ocr_pdf
from bibox_to_pdf.values.Constants import Constants
from rich import print


def main(
        username: Annotated[str, typer.Argument()],
        password: Annotated[str, typer.Argument()],
        book_id: Annotated[int, typer.Argument()],
        do_ocr: Annotated[bool, typer.Option(help="Don't do ocr on the generated pdf", default=False)]):

    book_dest_path = Constants.bookBaseOutputDir.format(book_id)
    print(f"Downloading book with id '{book_id}' to '{book_dest_path}'...")

    access_token = login_to_bibox(username, password)

    bibox_images = get_bibox_images(access_token, book_id)
    image_paths = download_images_from_bibox(bibox_images, book_id)
    pdf_non_ocr_path = create_pdf_from_images(book_id, image_paths)

    if do_ocr:
        ocr_pdf(book_id, pdf_non_ocr_path)


if __name__ == "__main__":
    typer.run(main)

import os
import requests
import typer
from bibox_to_pdf.values.Constants import Constants
from rich import print
from rich.progress import track


def get_bibox_images(access_token: str, book_id: int):
    headers = {"Authorization": f"Bearer {access_token}"}
    url = Constants.biboxBookInfoUrl.format(book_id)

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Response code from server was not 200. "
              f"Either the book id '{book_id}' doesn't exist or the login wasn't successful. "
              f"Exiting!")
        raise typer.Exit(1)

    return pages_to_image_array(response.json().get("pages", []))


def download_images_from_bibox(bibox_images: [], book_id: int):
    image_output_dir = Constants.imageOutputDir.format(book_id)
    os.makedirs(image_output_dir, exist_ok=True)

    options = {"responseType": "arraybuffer"}

    print(f"Starting download of {len(bibox_images)} images")

    image_paths = []
    index = 1
    for bibox_image in track(bibox_images, description="Downloading images..."):
        image_response = requests.get(bibox_image["url"], options)
        image_binary = image_response.content

        image_path = Constants.imageOutputFile.format(book_id, index)

        with open(image_path, "wb") as image_file:
            image_file.write(image_binary)

        image_paths.append(image_path)

        index += 1

    print(f"\nSuccessfully completed the download of {len(image_paths)} images!")
    return image_paths


def pages_to_image_array(pages: []):
    images = []
    for page in pages:
        image = page["images"][0] if page.get("images") else None
        if image is None:
            print("At least one image was null. Maybe script needs updating. Exiting!")
            raise typer.Exit(1)
        images.append(image)

    return images

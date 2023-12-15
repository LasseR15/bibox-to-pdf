<a name="readme-top"></a>

[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GPL-3.0 License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">BiBox to PDF</h3>

  <p align="center">
    CLI tool to download a book from BiBox as a OCR PDF
    <br />
    <br />
    <a href="https://github.com/LasseR15/bibox-to-pdf/issues">Report Bug</a>
    ·
    <a href="https://github.com/LasseR15/bibox-to-pdf/issues">Request Feature</a>
  </p>
</div>


<!-- DISCLAIMER -->
<div align="center">
  <h3>DISCLAIMER: THIS PROJECT IS FOR EDUCATIONAL PURPOSES ONLY</h3>
</div>
<br />

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites-for-manual-setup">Prerequisites for manual setup</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#usage-with-Docker">Usage with Docker</a></li>
        <li><a href="#usage-with-manual-setup">Usage with manual setup</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This cli script allows you to download and ocr books from [BiBox](https://www.bibox.schule/).

You need valid login credentials as well as access to the books you want to download.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
You can currently only run the script via Docker.

In the future there will be a described way to run it manually.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage


### Finding the book id
To find the book id, head over to https://bibox.schule and log in to your account. Now open the book you want to download. <br>
The url in your browser should look something like: `https://bibox2.westermann.de/book/5417/page/1`. <br>
Here the book id is `5417` (between the "/book/" and "/page/" section of the url).

### Usage with Docker
To run the image via Docker you can either do it directly via the Docker cli or the recommended way Docker compose.

There are two variants/tags available:
1. `latest`: The latest ocr version Docker image (larger image than the non-ocr verison)
2. `latest-non-ocr`: The latest non-ocr version. This image has no support for pdf ocr and is therefore smaller than the ocr version (Currently not available)

#### Docker Compose
To use the ocr version of the script with Docker Compose run the following command:
```bash
docker compose run --rm -it bibox-to-pdf \
    '{USERNAME}' '{PASSWORD}' {BOOK_ID}
```
<!-- CURRENTLY NOT AVAILABLE
If you want to run the non-ocr version run the following command.

You can also simply add `--no-ocr` before the username in the above command.
```bash
docker compose -f ./docker-compose.non-ocr.yml --rm -it run bibox-to-cli \
    '{USERNAME}' '{PASSWORD}' {BOOK_ID}
```
-->
#### Docker CLI
To use the script with ocr via Docker run the following command:
```bash
docker run --rm -it \
    -v ./books:/app/output/books \
    ghcr.io/lasser15/bibox-to-pdf:latest \
    '{USERNAME}' '{PASSWORD}' {book_id}
```
<!-- CURRENTLY NOT AVAILABLE
To use it without ocr, run the following command.

You can also simply add `--no-ocr` before the username in the above command.
```bash
docker run --rm -it \
    -v ./books:/app/output/books \
    ghcr.io/lasser15/bibox-to-pdf:latest-non-ocr \
    '{USERNAME}' '{PASSWORD}' {book_id}
```
-->

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Usage with manual setup
The manual setup is currently not supported. Please use Docker instead.


<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- LICENSE -->
## License
Distributed under the GPL 3.0 License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[stars-shield]: https://img.shields.io/github/stars/LasseR15/bibox-to-pdf.svg?style=for-the-badge
[stars-url]: https://github.com/LasseR15/bibox-to-pdf/stargazers
[issues-shield]: https://img.shields.io/github/issues/LasseR15/bibox-to-pdf.svg?style=for-the-badge
[issues-url]: https://github.com/LasseR15/bibox-to-pdf/issues
[license-shield]: https://img.shields.io/github/license/LasseR15/bibox-to-pdf.svg?style=for-the-badge
[license-url]: https://github.com/LasseR15/bibox-to-pdf/blob/release/LICENSE

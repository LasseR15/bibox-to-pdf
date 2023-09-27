import os


class Constants:
    biboxLoginUrl = 'https://bibox2.westermann.de'
    biboxBookInfoUrl = 'https://backend.bibox2.westermann.de/v1/api/sync/{}?materialtypes[]=default&materialtypes[]=addon'

    baseOutputPath = os.getenv('BASE_OUTPUT_PATH', default='.')
    bookBaseOutputDir = baseOutputPath + '/books/{}'
    imageOutputDir = bookBaseOutputDir + '/images/'
    imageOutputFile = imageOutputDir + '{}.png'
    pdfOutputDir = bookBaseOutputDir + '/pdfs/'
    pdfOutputFile = pdfOutputDir + '{}.pdf'

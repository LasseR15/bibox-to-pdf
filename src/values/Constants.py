class Constants:
    biboxLoginUrl = 'https://bibox2.westermann.de'
    biboxBookInfoUrl = 'https://backend.bibox2.westermann.de/v1/api/sync/{}?materialtypes[]=default&materialtypes[]=addon'
    # biboxBookPageUrl = 'https://bibox2.westermann.de/book/{{bookId}}/page/{pageNumber}'

    bookBaseOutputDir = '../books/{}'
    imageOutputDir = bookBaseOutputDir + '/images/'
    imageOutputFile = imageOutputDir + '{}.png'
    pdfOutputDir = bookBaseOutputDir + '/pdfs/'
    pdfOutputFile = pdfOutputDir + '{}.pdf'

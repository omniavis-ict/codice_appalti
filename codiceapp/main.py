from codiceapp.extract_to_text import pdf_to_text, pdf_to_text_allegati
from codiceapp.extract_articles import remove_page_number_and_other_noise_text, extract_articles, export
from loguru import logger


def start():
    logger.info("Starting app")
    pdf_file = open('Codiceappalti-Dlgs362023.pdf', 'rb')
    logger.info("pfd to text")
    text = pdf_to_text(pdf_file)
    lines = text.splitlines()
    logger.info("remove page number and other noise text")
    lines = remove_page_number_and_other_noise_text(lines)
    logger.info(lines[0:100])

    logger.info("extract articles")
    elenco, testo_articoli = extract_articles(lines)
    logger.info(elenco)
    logger.info("export to csv, json, xlsx")
    export(elenco, testo_articoli)
    logger.info("Done")

def start_allegati():
    logger.info("Starting app")
    pdf_file = open('Codiceappalti-Dlgs362023.pdf', 'rb')
    logger.info("pfd to text")
    text = pdf_to_text_allegati(pdf_file)
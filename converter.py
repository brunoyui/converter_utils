import logging

from reader import ReaderCSV
from writer import WriterCSV, WriterExcel, WriterConsole, WriterSQLFirst, WriterJsonLikeSpider, WriterJsonLikeSpiderFirst, WriterSQL

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


DATASET_FILE_PATH = "./data/dataset.tsv"

DATASET_FILE_WRITE_PATH_CSV = './data/datasetSQL.tsv'
DATASET_FILE_WRITE_PATH_EXCEL = './data/dataset_.xlsx'
DATASET_FILE_WRITE_PATH_JSON = './data/dataset.json'
DATASET_FILE_WRITE_PATH_SQL = './data/gold.txt'

def convert() -> None:
    dataset = read()
    write(dataset)

def read():
    reader = ReaderCSV()
    return reader.read(DATASET_FILE_PATH)

def write(dataset):
    #writer = WriterExcel()
    #writer = WriterConsole()
    #writer = WriterJsonLikeSpiderFirst()
    writer = WriterSQL()
    print(len(dataset))
    writer.write(dataset, DATASET_FILE_WRITE_PATH_SQL, 'events_log')


def main() -> None:
    logger.info("Start loading process")
    convert()
    logger.info("Finish loading process")


if __name__ == "__main__":
    main()

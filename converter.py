import logging

from reader import ReaderCSV
from writer import WriterCSV, WriterExcel, WriterConsole

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


DATASET_FILE_PATH = "./data/dataset.tsv"

DATASET_FILE_WRITE_PATH_CSV = './data/datasetSQL.tsv'
DATASET_FILE_WRITE_PATH_EXCEL = './data/dataset_.xlsx'

def convert() -> None:
    dataset = read()
    write(dataset)

def read():
    reader = ReaderCSV()
    return reader.read(DATASET_FILE_PATH)

def write(dataset):
    #writer = WriterExcel()
    writer = WriterConsole()
    print(len(dataset))
    writer.write(dataset)


def main() -> None:
    logger.info("Start loading process")
    convert()
    logger.info("Finish loading process")


if __name__ == "__main__":
    main()

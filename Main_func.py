import logging
from PyPDF2 import PdfFileMerger
import os
logging.basicConfig(filename = 'test.log', level = logging.DEBUG, format = "%(asctime)s %(levelname)s %(message)s")

def all_file(dir):
    """Function to return files in a directory"""
    path = os.listdir(dir)
    pdfs = []
    try:
        for i in path:
                pdfs.append(i)
        return pdfs
    except Exception as e:
        print(e)
        logging.error("Error occured {}".format(e))





print(os.getcwd())


def merger(files):
    """Program to merge pdfs"""
    merger_main = PdfFileMerger()
    try:
        for i in files:
            if i.endswith('pdf'):
                merger_main.append(i)
        merger_main.write('Merged_file.pdf')
        merger_main.close()
    except Exception as e:
        logging.error("Error occured {}".format(e))
        print(e)

print(all_file("C:\\Users\\ashuc"))


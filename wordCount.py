import logging
import sys
import re
import os

cwd = os.path.dirname(os.path.realpath(__file__))

def read():
    if len(sys.argv) is not 4:
        logging.info("Correct usage: wordCountTest.py <input text file> <output file> <solution key file>")
        #exit()
    logging.debug('read(): Instantiated')
    logging.debug(cwd)
    logging.debug(os.path.exists('e:\OS\Lab1\python-intro-cjuare01\speech.txt'))
    logging.debug(sys.argv[1])
    logging.debug()
    logging.debug('read(): Complete')
    return 0

if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s:%(message)s', level = logging.DEBUG)
    logging.debug('main(): Instantiated')
    read()
    logging.debug('main(): Complete')
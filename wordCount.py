import logging
import sys
import re
import os

inputFileName = sys.argv[1]
outputFileName = sys.argv[2]
wordDict = {}

def read():
    logging.debug('read(): Instantiated')
    inputFile = open(inputFileName, 'r')
    inputFileLine = inputFile.readlines()
    for line in inputFileLine:
        tempList = re.split(' ', line)
        logging.debug(tempList)
        logging.debug(line)
    logging.debug(sys.argv[1])
    logging.debug(sys.argv[2])
    logging.debug('read(): Complete')
    return 0

if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s:%(message)s', level = logging.DEBUG)
    logging.debug('main(): Instantiated')
    read()
    logging.debug('main(): Complete')
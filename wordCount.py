import collections
import logging
import sys
import re
import os

class WordCount():
    inputFileName = sys.argv[1]
    outputFileName = sys.argv[2]
    wordDict = {}

    def __init__(self):
        logging.debug('init(): Instantiated')
        self.read()
        self.write_output()
        logging.debug('init(): Complete')

    def read(self):
        logging.debug('read(): Instantiated')
        inputFile = open(self.inputFileName, 'r')
        inputFileLine = inputFile.readlines()
        self.line_manipulation(inputFileLine)
        inputFile.close()
        logging.debug('read(): Complete')
        return 0

    def line_manipulation(self, inputFileLine):
        logging.debug('line_manipulation(): Instantiated')
        for line in inputFileLine:
            tempList = re.split('\W+', line)
            for word in tempList:
                #if a new line was found inside the word, strip it
                if re.search('\n', word):
                    word = word.rstrip()
                word = word.lower()
                #if the word is not found in the dictionary it inserts the word and set's it to 0
                if not word in self.wordDict:
                    self.wordDict[word] = 0
                #when a word is found it increases it's value by one
                if word in self.wordDict:
                    self.wordDict[word] += 1
        self.wordDict = collections.OrderedDict(sorted(self.wordDict.items()))
        del self.wordDict['']
        logging.debug(self.wordDict)
        logging.debug('line_manipulation(): Complete')
        return 0
    
    def write_output(self):
        logging.debug('write_output(): Instantiated')
        outputFile = open('myOutput.txt', 'w+')
        for word in self.wordDict:
            outputFile.write(word+' '+str(self.wordDict[word])+'\n')
        #os.fsync(outputFile)
        outputFile.close()
        logging.debug('write_output(): Complete')
        return 0

if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s:%(message)s', level = logging.DEBUG)
    logging.debug('main(): Instantiated')
    WordCount()
    logging.debug('main(): Complete')
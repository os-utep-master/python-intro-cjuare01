import logging

if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s:%(message)s', level = logging.DEBUG)
    logging.debug('hello')
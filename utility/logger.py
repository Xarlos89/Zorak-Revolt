"""
Controls the logging for the entire application.
"""
import logging
import pathlib


log_file_path = pathlib.Path('utility/Zorak_logs.txt')
logging.basicConfig(filename=log_file_path,
                    format='%(asctime)s - %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M.%S',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def log_debug(thing: object):
    """ Logs at the debug level """
    logger.debug(thing)


def log_info(thing: object):
    """ Logs at the info level """
    print(thing)
    logger.info(thing)


def log_warn(thing: object):
    """ Logs at the warn level """
    print(thing)
    logger.warning(thing)


def log_critical(thing: object):
    """ Logs at the critical level """
    print(thing)
    logger.critical(thing)

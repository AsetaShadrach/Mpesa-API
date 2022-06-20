import logging 
import yaml
import os

file_path = "logs.log"

def create_log_file(filepath):
    path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(path, filepath)
    return logging.FileHandler(filename=filepath)

def make_logger(LOGGER):
    path = os.path.dirname(os.path.realpath(__file__))

    # Config file relative to this file
    loggingConf = open('{0}/logging.yml'.format(path), 'r')
    logging.config.dictConfig(yaml.safe_load(loggingConf.read()))
    loggingConf.close()

    return logging.getLogger(LOGGER)

    
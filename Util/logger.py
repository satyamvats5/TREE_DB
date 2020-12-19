import os
import sys
import logging
from logging import handlers


class Logger:
    
    def __init__(self):
        pass
    
    def __logger_path(self, filename=None):
        script_directory = os.path.dirname(os.path.abspath(__file__))
        script_name = os.path.basename(__file__)

        # Logs directory setup
        logs_directory = os.path.join(script_directory, 'logs')
        if not os.path.exists(logs_directory):
            os.makedirs(logs_directory)

        # Logging - File Handler
        log_file_size_in_mb = 10
        count_of_backups = 5  # example.log example.log.1 example.log.2
        log_file_size_in_bytes = log_file_size_in_mb * 1024 * 1024

        if filename == None:
            log_filename = os.path.join(logs_directory, os.path.splitext(script_name)[0]) + '.log'
        else:
            log_filename = os.path.join(logs_directory, filename) + '.log'
        
        return log_filename, log_file_size_in_bytes, count_of_backups
    
    def __setup_logger(self, name: str, filename: str=None):
        log_filename, log_file_size_in_bytes, count_of_backups = self.__logger_path(filename)
        # LOGGING
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        log_template = '%(asctime)s %(module)s %(levelname)s: %(message)s'
        formatter = logging.Formatter(log_template)
        file_handler = handlers.RotatingFileHandler(log_filename, maxBytes=log_file_size_in_bytes,
                                                backupCount=count_of_backups)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        # Logging - STDOUT Handler
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setFormatter(formatter)

        if not len(logger.handlers):
            logger.addHandler(stdout_handler)
            logger.addHandler(file_handler)

        return logger

    @property
    def get_network_logger(self):
        logger = self.__setup_logger(name="network", filename="networks")
        return logger
    
    @property
    def get_application_logger(self):
        logger = self.__setup_logger(name="application", filename="application")
        return logger

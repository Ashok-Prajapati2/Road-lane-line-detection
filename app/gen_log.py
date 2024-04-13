import logging
import os

class Logger:
    def __init__(self, log_dir='results/logs', log_file='app.log'):
        self.log_dir = log_dir
        self.log_file = log_file
        self.setup_logging()

    def setup_logging(self):
        os.makedirs(self.log_dir, exist_ok=True)
        logging.basicConfig(filename=os.path.join(self.log_dir, self.log_file),
                            level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def log_info(self, message):
        logging.info(message)

    def log_warning(self, message):
        logging.warning(message)

    def log_error(self, message):
        logging.error(message)

    def log_exception(self, message):
        logging.exception(message)

    def log_debug(self, message):
        logging.debug(message)

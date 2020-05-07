import logging


# Example of creating a custom logger which has FileHandler

tst_logger = logging.getLogger('test_logger_python')
tst_logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('test_logger_python.log')
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
tst_logger.addHandler(fh)

tst_logger.error("THIS IS CUSTOM LOG!!!")

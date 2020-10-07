import logging

logger = logging.getLogger(__name__)

def configure():
    raise Exception("test")

def start():
    try:
        # do something
        configure()
    except Exception as error:
        logger.error(error)
        # exception will be raised exactly as it was
        raise

if __name__ == "__main__":
    start()
import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class MyApp:

    def __init__(self, name: str):
        self.name = name

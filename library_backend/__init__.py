import logging

from sqlalchemy.ext.declarative import declarative_base

logging.basicConfig(level=logging.ERROR,
                    format="%(asctime)s - %(module)s::%(funcName)s - [%(levelname)s] - %(message)s")
logger = logging.getLogger("LibraryBackend")

Base = declarative_base()

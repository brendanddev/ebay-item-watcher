
# test_logger.py
from logger import Logger
import logging

def test_custom_logger():
    my_logger = Logger(
        name="[TestLogger]",
        name_color="cyan",
        level=logging.DEBUG,
        to_console=True,
        to_file=False
    ).get_logger()

    my_logger.debug("This is a DEBUG message")
    my_logger.info("This is an INFO message")
    my_logger.warning("This is a WARNING message")
    my_logger.error("This is an ERROR message")
    my_logger.critical("This is a CRITICAL message")

if __name__ == "__main__":
    test_custom_logger()


""" 
color_console_handler.py
A custom logging handler to output colored logs without external libraries

Brendan Dileo - July 2025
"""
import logging
import sys

class ColorConsoleHandler(logging.StreamHandler):
    
    # Log level color codes
    COLOR_CODES = {
        logging.DEBUG: "\033[1;36m",
        logging.INFO: "\033[1;32m",
        logging.WARNING: "\033[1;33m",
        logging.ERROR: "\033[1;31m",
        logging.CRITICAL: "\033[1;41m",
        "RESET": "\033[0m"
    }
    
    # Intializes instance of the handler and makes call to parent to 
    # set stream for output
    def __init__(self):
        super().__init__(sys.stdout)
    
    # Overrides parent implementation to provide custom color formatting
    def emit(self, record):
        try:
            # Formats the log record and gets current color code
            msg = self.format(record)
            color = self.COLOR_CODES.get(record.levelno, self.COLOR_CODES["RESET"])
            # Write colored message to the console with reset
            self.stream.write(f"{color}{msg}{self.COLOR_CODES['RESET']}\n")
            self.flush()
        except Exception:
            # Call parent method to handle errors
            self.handleError(record)
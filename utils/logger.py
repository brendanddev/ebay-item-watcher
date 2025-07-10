
"""
logger.py
A custom configurable loggier for the ebay item watcher

Brendan Dileo - July 2025
"""

import logging

from color_console_handler import ColorConsoleHandler

class Logger:
    
    # Creates an instance of the logger
    def __init__(
        self,
        name="[ebayWatcher]",
        name_color="blue",
        level=logging.INFO,
        to_console=True,
        to_file=False,
        file_name="ebay_watcher.log",
        timestamp_format="%Y-%m-%d %H:%M:%S",
    ):
        
        # Set instance vars and prevent duplicate loggers
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        # stop log mesages from being passed to parent loggers
        self.logger.propagate = False
        
        # If no handlers are attached to the logger instance
        # conditionally add console or file handler
        if not self.logger.handlers:
            
            # Default format for log messages
            formatter = logging.Formatter(
                f"%(asctime)s - {self(name, name_color)} - %(levelname)s - %(message)s",
                datefmt=timestamp_format,
            )
            
            # Console output
            if to_console:
                console_handler = ColorConsoleHandler()
                console_handler.setFormatter(formatter)
                self.logger.addHandler(console_handler)
            
            # File output
            if to_file:
                file_handler = logging.FileHandler(file_name)
                file_handler.setFormatter(formatter)
                self.logger.addHandler(file_handler)
    
    # Get current instance of the logger
    def get_logger(self):
        return self.logger
    
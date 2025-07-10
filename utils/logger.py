
"""
logger.py
A custom configurable loggier for the ebay item watcher

Brendan Dileo - July 2025
"""

import sys
import logging

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
            
            formatter = logging.Formatter(
                f"%(asctime)s - {self._colorize(name, name_color)} - %(levelname)s - %(message)s",
                datefmt=timestamp_format,
            )
            
            if to_console:
            if to_file:
    
    # Get current instance of the logger
    def get_logger(self):
        return self.logger
    
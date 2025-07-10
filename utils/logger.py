
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
                f"%(asctime)s - {self._colorize(name, name_color)} - %(levelname)s - %(message)s",
                datefmt=timestamp_format,
            )
            
            if to_console:
                console_handler = ColorConsoleHandler()
                console_handler.setFormatter(formatter)
                self.logger.addHandler(console_handler)
            
            if to_file:
                file_handler = logging.FileHandler(file_name)
                file_handler.setFormatter(formatter)
                self.logger.addHandler(file_handler)
    
    # Adds color to the logegr name in console
    def _colorize(self, text, color_name):
        colors = {
            "red": "\033[91m",
            "green": "\033[92m",
            "yellow": "\033[93m",
            "blue": "\033[94m",
            "magenta": "\033[95m",
            "cyan": "\033[96m",
            "reset": "\033[0m",
        }
        color_code = colors.get(color_name.lower(), "")
        reset_code = colors["reset"] if color_code else ""
        return f"{color_code}{text}{reset_code}"
    
    # Get current instance of the logger
    def get_logger(self):
        return self.logger
    
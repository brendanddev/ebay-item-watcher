
"""
logger.py
A custom configurable loggier for the ebay item watcher

Brendan Dileo - July 2025
"""

import sys
import logging
import cachetools

try:
    from colorama import Fore, Style, init as colorama_init
    colorama_init()
except ImportError:
    Fore = Style = None


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
        pass
    
    # Get current instance of the logger
    def get_logger(self):
        return self.logger
    
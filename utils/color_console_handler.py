
""" 
color_console_handler.py
A custom logging handler to output colored logs without external libraries

Brendan Dileo - July 2025
"""
import logging
import sys

class ColorConsoleHandler(logging.StreamHandler):
    
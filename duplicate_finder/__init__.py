"""
duplicate-finder - Find duplicate records in datasets

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import DuplicateFinder, find, process, main

__all__ = ["DuplicateFinder", "find", "process", "main"]

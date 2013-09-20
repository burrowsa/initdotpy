"""Tests importing modules with __all__ non empty"""

__all__ = ['fox']

from initdotpy import auto_import
auto_import(__name__, __file__)
del auto_import

def fox():
    return "fox"

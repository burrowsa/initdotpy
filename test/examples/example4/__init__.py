"""Tests importing module contents with no __all__ defined in one module"""
from initdotpy import auto_import_contents
auto_import_contents(__name__, __file__)

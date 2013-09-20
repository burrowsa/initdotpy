"""Tests importing module contents with no __all__ defined in one module"""
from initdotpy import auto_import
auto_import(__name__, __file__, True)
del auto_import

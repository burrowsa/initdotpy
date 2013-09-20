"""Tests importing module contents with a duplicate name"""
from initdotpy import auto_import
auto_import(__name__, __file__, True)
del auto_import

"""Tests importing module contents"""
from initdotpy import auto_import
auto_import(__name__, __file__, True)
del auto_import

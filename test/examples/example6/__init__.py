"""Tests using auto_import on multiple levels of packages"""
from initdotpy import auto_import
auto_import(__name__, __file__, True)
del auto_import

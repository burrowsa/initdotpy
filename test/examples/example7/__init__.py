"""Test excluding a module"""

from initdotpy import auto_import
auto_import(__name__, __file__, exclude=set(['module13']))
del auto_import

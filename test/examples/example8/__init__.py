"""Test function is automatically removed even if it is renamed"""

from initdotpy import auto_import as some_other_name
some_other_name(__name__, __file__)

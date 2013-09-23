"""Test combining auto_import and auto_import_contents in the same __init__.py the other way around"""

from initdotpy import auto_import,auto_import_contents
auto_import_contents()
auto_import()


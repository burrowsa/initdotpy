"""Test function is automatically removed even if it is imported under several names"""

from initdotpy import auto_import
from initdotpy import auto_import as some_other_name
from initdotpy import auto_import as any_name_you_like
auto_import()

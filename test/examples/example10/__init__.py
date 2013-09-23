"""Test function is not automatically removed if it is mentioned in __all__"""

from initdotpy import auto_import
from initdotpy import auto_import as some_other_name
from initdotpy import auto_import as any_name_you_like
from initdotpy import auto_import as this_one_gets_through


__all__ = ['this_one_gets_through']


auto_import()


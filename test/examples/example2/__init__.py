"""Tests importing modules with __all__ non empty"""


__all__ = ['fox']


def fox():
    return "fox"


from initdotpy import auto_import
auto_import()

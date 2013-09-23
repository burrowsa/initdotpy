"""The initdotpy package makes it simple to write __init__.py files that automatically include the package contents.

For example if you have an __init__.py that looks like::

import submodule1 
import submodule2 
import submodule3 
import subpackage1
import subpackage2
import subpackage3

You can replace it with::

from initdotpy import auto_import
auto_import(__name__, __file__)

and it will automatically import all the modules/packages contained in the package and stay up to date when you make changes to the package contents.

Or if you prefer to import the contents of the submodules/subpackages, e.g.::

from submodule1 import *
from submodule2 import *
from submodule3 import *
from subpackage1 import *
from subpackage2 import *
from subpackage3 import *

You can just write your __init__.py as::

from initdotpy import auto_import_contents
auto_import_contents(__name__, __file__)

Again this __init__.py automatically stays up to date so you need never edit it again."""
import os
import sys
import pkgutil
 
 
__all__ = ['auto_import', "auto_import_contents"]


def auto_import(parent, filename, exclude=tuple()):
    """If you have an __init__.py that looks like::
    
    import submodule1 
    import submodule2 
    import submodule3 
    import subpackage1
    import subpackage2
    import subpackage3
    
    You can replace it with::
    
    from initdotpy import auto_import
    auto_import(__name__, __file__)
    
    and it will automatically import all the modules/packages contained in the package and stay up to date when you make changes to the package contents."""
    _auto_import(parent, filename, False, exclude, auto_import)


def auto_import_contents(parent, filename, exclude=tuple()):
    """If you have an __init__.py that looks like::
    
    from submodule1 import *
    from submodule2 import *
    from submodule3 import *
    from subpackage1 import *
    from subpackage2 import *
    from subpackage3 import *
    
    You can just write your __init__.py as::
    
    from initdotpy import auto_import_contents
    auto_import_contents(__name__, __file__)
    
    and it will automatically import the contents from all the modules/packages contained in the package and stay up to date when you make changes to the package contents."""
    _auto_import(parent, filename, True, exclude, auto_import_contents)

 
def _auto_import(parent, filename, import_contents, exclude, item_for_removal):
    parent_module = sys.modules[parent]
 
    if not hasattr(parent_module, '__all__'):
        parent_module.__all__ = []
 
    for module_loader, child, _ in pkgutil.iter_modules([os.path.dirname(filename)]):
        if child not in exclude:
            child_module = module_loader.find_module(parent + '.' + child).load_module(parent + '.' + child)
            if import_contents:
                if not hasattr(child_module, '__all__'):
                    raise RuntimeError("Module or package %s does not define __all__" % child)
     
                duplicates = set(child_module.__all__).intersection(parent_module.__all__)
                if duplicates:
                    raise RuntimeError("The following names, defined in %s, are already defined elsewhere: %s"
                                       % (child, duplicates))
                else:
                    for name in child_module.__all__:
                        setattr(parent_module, name, getattr(child_module, name))
                        parent_module.__all__.append(name)
            else:
                setattr(parent_module, child, child_module)
                parent_module.__all__.append(child)

    for attr_name in dir(parent_module):
        attr_value = getattr(parent_module, attr_name)
        if attr_value is item_for_removal and attr_name not in parent_module.__all__:
            delattr(parent_module, attr_name)

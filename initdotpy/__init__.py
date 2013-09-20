import os
import sys
import pkgutil
 
 
__all__ = ['auto_import']
 
 
def auto_import(parent, filename, import_contents=False, exclude=tuple()):
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

import pathlib
from importlib import import_module
from inspect import getmembers, isclass
from os import walk
from os.path import abspath, basename, dirname, join

PROJ_DIR = pathlib.Path(__file__).parent.parent.parent.parent
APP_MODULE = basename(PROJ_DIR)


def get_modules(module):
    """Returns all .py modules in given file_dir that are not __init__."""
    file_dir = abspath(join(PROJ_DIR, module))
    for root, dirnames, files in walk(file_dir):
        mod_path = "{}{}".format(APP_MODULE, root.split(PROJ_DIR)[1]).replace("/", ".")
        for filename in files:
            if filename.endswith(".py") and not filename.startswith("__init__"):
                yield ".".join([mod_path, filename[0:-3]])


def dynamic_loader(module, compare):
    """Iterates over all .py files in `module` directory, finding all classes that
    match `compare` function.
    Other classes/objects in the module directory will be ignored.

    Returns unique items found.
    """
    items = []
    for mod in get_modules(module):
        module = import_module(mod)
        if hasattr(module, "__all__"):
            objs = [getattr(module, obj) for obj in module.__all__]
            items += [o for o in objs if compare(o) and o not in items]
    return items

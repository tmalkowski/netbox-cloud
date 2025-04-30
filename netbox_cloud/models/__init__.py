import os
import re
import importlib

__all__ = []

_pkg = __name__          # e.g. "yourpackage.models"
_pkg_dir = os.path.dirname(__file__)

for fname in os.listdir(_pkg_dir):
    if not fname.endswith('.py') or fname == '__init__.py':
        continue

    module_name = fname[:-3]
    path = os.path.join(_pkg_dir, fname)

    # pull out all top-level class names
    with open(path, 'r') as f:
        classes = re.findall(r'^class\s+([A-Za-z_][A-Za-z0-9_]*)', f.read(), re.MULTILINE)

    if not classes:
        continue

    # import the module once
    module = importlib.import_module(f'.{module_name}', _pkg)

    # bind each class into this namespace
    for cls in classes:
        globals()[cls] = getattr(module, cls)
        __all__.append(cls)


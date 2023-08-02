# Create Packages in Python
# my_package/__init__.py
from . import module1
from .sub_package import module2
__all__ = ["module1", "module2"]
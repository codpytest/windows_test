# from __future__ import annotations
from setuptools import Extension
from setuptools import setup
from Cython.Build import cythonize
__version__ = '0.0.1'



setup(ext_modules=cythonize([Extension(name="printf", sources=["src/printf.c"])]))
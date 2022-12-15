# from __future__ import annotations
from setuptools import Extension
from setuptools import setup
# from Cython.Build import cythonize
import pybind11
__version__ = '0.0.1'


printf = Extension(
    'printf',
    sources=["src/printf.c"],
    extra_compile_args = ['-std=c++14'],
    include_dirs=[pybind11.get_include()],
)

if __name__ == "__main__":
    setup(
        name = 'printf',
        ext_modules=[printf],
    )
# libprint = setup(ext_modules=cythonize([Extension(name="printf", sources=["src/printf.c"])]))
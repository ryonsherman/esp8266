#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"
__version__   = "1.0" # setup version

import os
import sys

from setuptools import setup

# get app version
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
from lua_loader import __version__ as VERSION

# windows platform
if sys.platform.startswith('win'):
    pass
# mac platform
elif sys.platform.startswith('darwin'):
    pass
# linux platform
elif sys.platform.startswith('linux'):
    options = dict(
        packages=[
            'lua_loader',
            'lua_loader.ui',
            'lua_loader.widget'
        ],
        package_dir={'lua_loader': 'src/lua_loader'},
        entry_points={'console_scripts': ['lua_loader = lua_loader:main']}
    )
# unsupported platform
else: raise Exception("platform unsupported")

# perform setup
setup(
    author="Ryon Sherman",
    author_email="ryon.sherman@gmail.com",
    name="LuaLoader",
    description="ESP8266 LUA Loader",
    #long_description=open('README.md').read(),
    #url="https://github.com/ryonsherman/noise",
    version=VERSION,
    #install_requires=['dep'],
    **options
)

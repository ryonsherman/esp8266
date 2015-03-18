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
from node_gui import __version__ as _version_

# handle windows platform
if sys.platform.startswith('win'):
    pass
# handle mac platform
elif sys.platform.startswith('darwin'):
    pass
# handle linux platform
elif sys.platform.startswith('linux'):
    options = dict(
        packages=[
            # application
            'node_gui',
            'node_gui.widget',
            'node_gui.dialog',
            'node_gui.window',
            # interface
            'node_gui.ui',
            'node_gui.ui.widget',
            'node_gui.ui.dialog',
            'node_gui.ui.window'
        ],
        package_dir={'node_gui': 'src/node_gui'},
        entry_points={'console_scripts': ['node_gui = node_gui:main']}
    )
# disallow unsupported platform
else: raise Exception("platform unsupported")

# perform setup
setup(
    author=__author__,
    author_email=__email__,
    name="NodeGUI",
    description="A Qt-based GUI for the ESP8266 NodeMcu environment",
    #long_description=open('README.md').read(),
    url="http://github.com/ryonsherman/esp8266/node_gui",
    version=_version_,
    install_requires=[
        'pyserial',
        'pygments',
        'humanize'
    ],
    **options
)

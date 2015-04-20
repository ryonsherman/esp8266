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
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
from esp8266.gui import __version__ as _version_

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
            'esp8266',            # library
            'esp8266.gui',        # application
            'esp8266.gui.ui',     # interface
            'esp8266.gui.widget', # interface widgets
        ],
        package_dir={'esp8266': 'src/esp8266'},
        entry_points={'console_scripts': ['esp8266-gui = esp8266.gui:main']}
    )
# disallow unsupported platform
else: raise Exception("platform unsupported")

# perform setup
setup(
    author=__author__,
    author_email=__email__,
    name="ESP8266 NodeMCU GUI",
    description="A Qt-based GUI for the ESP8266 NodeMCU environment",
    #long_description=open('README.md').read(),
    url="http://github.com/ryonsherman/esp8266/gui",
    version=_version_,
    install_requires=[
        'pyserial',
        'pygments',
        'humanize'
    ],
    **options
)

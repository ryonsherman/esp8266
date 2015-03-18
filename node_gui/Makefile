#!/usr/bin/env make
#
# Copyright 2015, Ryon Sherman <ryon.sherman@gmail.com>
# MIT License - http://opensource.org/licenses/MIT
# NodeGUI - http://github.com/ryonsherman/esp8266/node_gui
#
project = 'node_gui'
install:
	python2 setup.py install
uninstall:
	echo 'todo'
dep:
	#
	# Installing dependencies
	#
	pip2 install \
		setuptools \
		pyserial \
		pygments \
		humanize
	# Manually copy PyQt4 dependencies
	cp -r /usr/lib/python2.7/site-packages/PyQt4 ./dev/lib/python2.7/site-packages/
	cp /usr/lib/python2.7/site-packages/sip.so ./dev/lib/python2.7/site-packages/
	cp /usr/lib/python2.7/site-packages/sipconfig.py ./dev/lib/python2.7/site-packages/
	cp /usr/lib/python2.7/site-packages/sipdistutils.py ./dev/lib/python2.7/site-packages/
	#
	if [ -x "`which xsel`" ]; then \
		echo 'make install' | xsel --clipboard --input; \
	fi
	#
	# If the 'xsel' binary exists the previous text was copied to the clipboard for your convenience.
	#
dev:
	#
	# Creating virtual development environment
	#
	virtualenv2 dev
	#
	# NOTICE!
	#
	# You must manually execute 'source dev/bin/activate' to enable the virtual environment.
	#   Type 'deactivate' once complete.
	#
	# To provide dependencies type 'make dep'.
	#   To install, type 'make', 'make install', or 'python2 setup.py install' to package the module.
	#
	if [ -x "`which xsel`" ]; then \
		echo 'source dev/bin/activate; make dep' | xsel --clipboard --input; \
	fi
	#
	# If the 'xsel' binary exists the previous text was copied to the clipboard for your convenience.
	#
interface:
	#
	# Converting QT4 .ui files to python modules
	# TODO: # Converting QT4 .qrc files to python modules (pyrcc4)
	#
	for f in `find src -name *.ui`; do \
		pyuic4 "$$f" -o `dirname "$$f"`/`basename "$$f" .ui`.py; \
	done
	#
	# Converting QT4 .qrc files to python modules
	#
	for f in `find src -name *.qrc`; do \
		pyrcc4 "$$f" -o `dirname "$$f"`/`basename "$$f" .qrc`.py; \
	done
	#
	# Listing files
	#
clean:
	#
	# Removing virtual development environment and setup files.
	#
	rm -rf dev build dist *.egg-info *.log
	#
	# Removing compiled python files
	#
	find . -name "*.pyc" -exec rm -rf {} \;
	#
	# NOTICE!
	#
	# You must manually execute 'deactivate' to disable the virtual environment.
	#
	if [ -x "`which xsel`" ]; then \
		echo 'deactivate' | xsel --clipboard --input; \
	fi
	#
	# If the 'xsel' binary exists the previous text was copied to the clipboard for your convenience.
	#

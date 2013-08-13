#!/usr/bin/python
#
# vim: tabstop=4 expandtab shiftwidth=4 noautoindent
#
# Copyright (C) 2013 Steve Crook <steve@mixmin.net>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTIBILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup

setup(
    name='kmlmod',
    author='Steve Crook',
    author_email='steve@mixmin.net',
    version='0.1',
    packages=['kmlmod', ],
    scripts=['kmlmod/kmlmod', ],
    license='GPLv3',
    url='https://github.com/crooks/kmlmod',
    long_description=open('README').read(),
    #data_files=[('man/man1', ['man/pyclean.1'])],
)

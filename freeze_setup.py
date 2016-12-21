#!/usr/bin/python3
version="""\"0.3.0\"
"""
"""
This script is for creating a frozen version of the program.
This is useful for Windows so you can have a nice exe file to run
"""

from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

base = 'Console'

executables = [
    Executable('html2csv-script', base=base, targetName = 'html2csv.exe')
]

setup(name='html2csv',
version = version,
description = 'A simple HTML to CSV converter',
options = dict(build_exe = buildOptions),
executables = executables)

#!/usr/bin/python3
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

base = 'Console'

executables = [
    Executable('main.py', base=base, targetName = 'html2csv')
]

setup(name='html2csv',
      version = '0.2.0',
      description = 'a simple html to csv converter',
      options = dict(build_exe = buildOptions),
      executables = executables)

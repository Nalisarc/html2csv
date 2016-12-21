v="""\"0.3.0\"
"""
from setuptools import setup

setup(
    name="html2csv",
    version=v,
    description='A html to csv table converter',
    url='https://github.com/Nalisarc/html2csv',
    author='Daniel Alexander Smith',
    author_email='nalisarc@gmail.com',
    license='MIT',
    scripts=['bin/html2csv'],
    packages=['html2csv'],
    install_requires=[
        'bs4',
        'requests',
    ],
    zip_safe=False)

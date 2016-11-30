#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests

import sys
import re
import csv
import argparse

parser = argparse.ArgumentParser(description="Converts html tables into csv tables")

parser.add_argument("-v","--verbosity", help="Enables verbose mode, usefule for debugging.", action="store_true")
parser.add_argument("file", help="A file to read in", nargs='*')
#parser.add_argument("--ommit-column", help="Ommits a column from the output", nargs='+')

args = parser.parse_args()

if args.verbosity:
        print("Verbose mode enabled")
        def verboseprint(*args):
                for arg in args:
                        print(arg,)
                return None
else:
        verboseprint = lambda *a: None
"""
def url_reader(url):
        site = requests.get(url)
        return site.text
"""
def file_reader(file_):
        with open(file_, 'rb') as f:
                return f.read()
def cell_text(cell):
        # strips down the cell for read-ablility
        return " ".join(cell.stripped_strings)


def converter(in_, out):
        pattern = 't[dh]'
        with open(out,'w') as o: #Makes sure that file spawn before processing
                soup = BeautifulSoup(in_,'html.parser')
                output = csv.writer(o)
                table = soup.find('table')
                for row in table.find_all('tr'):
                        col = [cell_text(ele)
			       for ele in row.find_all(re.compile(pattern))
                        ]
                        col.remove(col[2])
                        output.writerow(col)
                        output.writerow([])

def main(args):
        if args.file:
                verboseprint("begining coversion process")
        else:
                verboseprint("No inputs specified")
                return 1

        if args.file:               
                for f in args.file:
                        verboseprint("Processing: {0}".format(f))
                        converter((file_reader(f)),(str(f) + ".csv"))

        """        
        if args.url:
                for u in args.url:
                        verboseprint("Processing: {0}".format(u))
                        converter(url_reader(u),(str(u) + ".csv"))"""
        return None
if __name__ == '__main__':
        main(args)
        sys.exit()

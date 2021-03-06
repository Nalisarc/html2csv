# Third Party Modules
from bs4 import BeautifulSoup
import requests

# Standard Library Modules
import argparse
import re
import csv
import sys

# functions

def file_reader(file_):
        #Opens a file and and returns the contents as a string

        with open(file_, 'rb') as f:
                return f.read()
        return 1
def url_reader(url, auth=None):
        site = requests.get(url)
        return site.text

from bs4 import BeautifulSoup
import re

def cell_text(cell):
        # strips down the cell for read-ablility
        return " ".join(cell.stripped_strings)


def html_parser(in_,):
        """
Takes an html string and searches for the first table.
Using regular expressions it finds all table rows and headers.
Then each cell of the found rows are striped and made into a list.
Then exports that those lists in a two by two list or a Dataframe if that name suites you better.
        """
        pattern = 't[dh]'
        output = []
        soup = BeautifulSoup(in_,'html.parser')
        table = soup.find('table')
        for row in table.find_all('tr'):
                col = [cell_text(ele)
		 for ele in row.find_all(re.compile(pattern))
		  ]
                output.append(col)

        return output
import csv
def csv_writer(in_, out):
        with open(out,'w') as o:
                output = csv.writer(o)
                for row in in_:
                        col = [ele for ele in row]
                        output.writerow(col)
                return None
        return 1

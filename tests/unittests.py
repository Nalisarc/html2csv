import unittests
import html2csv
import os
import sys

class UnitTests(unittest.TestCase):


    def test_can_read_file(self):

        test_read = html2csv.file_reader("tests/testcase.html")

        self.assertNotEqual(len(test_read),0)

    def test_can_read_url(self):

        test_read = url_reader("http://www.w3schools.com/html/html_tables.asp")

        self.assertNotEqual(len(test_read),0)

    def test_can_parse_html(self):

        file_input = html2csv.file_reader("tests/testcase.html")

        parsed_table = html2csv.html_parser(file_input)

        self.assertNotEqual(len(parsed_table),0)

        control_table = [["hello","world"][1,2]['a','b']]

        self.assertEqual(parsed_table,control_table)

    def test_can_write_to_output(self):

        file_input = html2csv.file_reader("tests/testcase.html")

        parsed_table = html2csv.html_parser(file_input)

        html2csv.csv_writer(parsed_table,"tests/testoutput.csv")

        with open("tests/testoutput.csv","r") as f:
            self.assertNotEqual(len(f.read()),0)

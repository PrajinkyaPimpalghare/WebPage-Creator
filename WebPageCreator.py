"""=======================================================================================
INFORMATION ABOUT CODE *Coding ISO9001:2015 Standards
==========================================================================================
For Creating basic webpage with minimal information with jinja2

Author: Prajinkya Pimpalghare

Date: 14-9-2017
Version: 1.1
Input Variable: Information about user
==========================================================================================="""
from __future__ import print_function
from jinja2 import Environment, FileSystemLoader
import os
from datetime import datetime as DT
from io import open


class WebPageCreator(object):
    def __init__(self):
        """
        Initializing important variables for WebPage creation.
        """
        self.basic_info = {"Name": "Person1", "About Me": "Coding Lover", "Age": "23"}
        self.personal_info = {"Name": "Person12", "About you": "Coder", "Age": "23"}

    def main(self):
        """
        Main Function which will create the report based on information given in xml file.
        """
        j2_env = Environment(loader=FileSystemLoader(os.path.dirname(os.path.abspath(__file__))), trim_blocks=True)
        output_test = j2_env.get_template('ReportModel.html').render(
            My_Report_Page="Welcome to My Page",
            basic_data=self.basic_info,
            personalinfo=self.personal_info,
            ID=str(DT.now()),
            age="0",
        )
        report = open("WebPage.html", "w+", encoding="latin-1")
        report.write(output_test)
        report.close()


# =================================================================================================
# =================================================================================================
# Main
# =================================================================================================
if __name__ == '__main__':
    REPORT_CREATION = WebPageCreator()
    REPORT_CREATION.main()
# =================================================================================================

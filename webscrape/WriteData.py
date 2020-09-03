import json
import requests  # get the html from websites
from bs4 import BeautifulSoup
from typing import Dict, List

def write_dictionary_data(course_dictionary: Dict[str, List[str]], subject: str) -> None:
    """
    Write the course's dictonary data to a file

    :course_dictionary: The dictionary containing the course information

    :subject: The subject of the course
    """

    file_name = subject + "_course_dictonary.txt"

    f = open(file_name, "w")
    f.write(json.dumps(course_dictionary, indent=4))
    # f.write(str(course_dictionary))
    f.close

def Output_HTML_Data(b: BeautifulSoup, subject: str) -> None:
    """
    Send the HTML data from BeautifulSoup and writes to a textfile in a nicely formatted way

    :b: a beautifulsoup object

    :subject: string that determines subject we're working with

    :kind: string that determines type of data that result_set holds (title, description, etc...)
    
    """
    file_name = "html_output_" + subject + ".html"
    # CSC HTML Output
    f = open(file_name, "w")
    f.write(str(b.prettify))
    f.write("\n")
    f.close


def write_set_data(result_set, subject: str, kind: str):
    """
    Iterate and print out the result of the result_set data

    :result_set: a result set from beautifulsoup4

    :subject: string that determines subject we're working with

    :kind: string that determines type of data that result_set holds (title, description, etc...)
    
    """
    file_name = subject + "_" + kind + "_set_output.txt"
    f = open(file_name, "w")
    for tag_data in result_set:
        f.write(str(tag_data.text) + ",\n")
    f.close

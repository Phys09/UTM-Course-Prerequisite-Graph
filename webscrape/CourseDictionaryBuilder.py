import requests  # get the html from websites
from bs4 import BeautifulSoup
from typing import Dict, List

def build_course_dictionary(title_result_set, desc_result_set) -> Dict[str, List[str]]:
    """
    Build a dictionary with the course name, and the description

    :param title_result_set: result set that holds title names for each course

    :param desc_result_set: The result set that holds the descriptions for each course

    :rtype: A dictionary with course names as keys, and a list for each line in description
    """

    course_dictionary = {}  # placeholder dictionary

    for (tagged_title, tagged_description) in zip(title_result_set, desc_result_set):  # iterate through multiple result sets
        course_dictionary[str(tagged_title.text)] = str(tagged_description.text).strip().splitlines()  # remove trailing whitespace, then get list of lines

    return course_dictionary
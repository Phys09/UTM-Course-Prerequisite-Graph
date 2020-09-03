import requests  # get the html from websites
import json
import WriteData as wd
import CourseDictionaryBuilder as cdb

from bs4 import BeautifulSoup

html_parser = 'html.parser'  # The HTML parser

# Links of the course information
csc_link = "https://student.utm.utoronto.ca/calendar/list_courses.pl?Depart=7"
mat_link = "https://student.utm.utoronto.ca/calendar/list_courses.pl?Depart=27"
sta_link = "https://student.utm.utoronto.ca/calendar/list_courses.pl?Depart=38"

# Store request objects for each of the links. HTML stored in these objects
request_csc = requests.get(csc_link)
request_mat = requests.get(mat_link)
request_sta = requests.get(sta_link)

# Make BeautifulSoup objects for each of the course subjects
csc_soup = BeautifulSoup(request_csc.text, html_parser)
mat_soup = BeautifulSoup(request_mat.text, html_parser)
sta_soup = BeautifulSoup(request_sta.text, html_parser)

# Get titles as a result set
csc_title_result_set = csc_soup.find_all('p', attrs={'class': 'titlestyle'})
mat_title_result_set = mat_soup.find_all('p', attrs={'class': 'titlestyle'})
sta_title_result_set = sta_soup.find_all('p', attrs={'class': 'titlestyle'})

# Get course descriptions as a result set
# Prerequisites are also in the descriptions
csc_desc_result_set = csc_soup.find_all('span', attrs={'class': 'normaltext'})
mat_desc_result_set = mat_soup.find_all('span', attrs={'class': 'normaltext'})
sta_desc_result_set = sta_soup.find_all('span', attrs={'class': 'normaltext'})

# Store course name, description as a dictionary
csc_courses = cdb.build_course_dictionary(csc_title_result_set, csc_desc_result_set)
mat_courses = cdb.build_course_dictionary(mat_title_result_set, mat_desc_result_set)
sta_courses = cdb.build_course_dictionary(sta_title_result_set, sta_desc_result_set)


if __name__ == "__main__":
    # First, we output the data to the file
    wd.Output_HTML_Data(csc_soup, "csc")
    wd.Output_HTML_Data(mat_soup, "mat")
    wd.Output_HTML_Data(sta_soup, "sta")

    # Output the titles to a txt file
    wd.write_set_data(csc_title_result_set, "csc", "title")
    wd.write_set_data(mat_title_result_set, "mat", "title")
    wd.write_set_data(sta_title_result_set, "sta", "title")

    # Output the descriptions to a txt file
    wd.write_set_data(csc_desc_result_set, "csc", "desc")
    wd.write_set_data(mat_desc_result_set, "mat", "desc")
    wd.write_set_data(sta_desc_result_set, "sta", "desc")

    # Output the dictionary to a txt file
    wd.write_dictionary_data(csc_courses, "csc")
    wd.write_dictionary_data(mat_courses, "mat")
    wd.write_dictionary_data(sta_courses, "sta")

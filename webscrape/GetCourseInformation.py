import requests  # get the html from websites
from bs4 import BeautifulSoup

csc_link = "https://student.utm.utoronto.ca/calendar/list_courses.pl?Depart=7"
mat_link = "https://student.utm.utoronto.ca/calendar/list_courses.pl?Depart=27"
sta_link = "https://student.utm.utoronto.ca/calendar/list_courses.pl?Depart=38"

# Store request objects for each of the links 
request_csc = requests.get(csc_link)
request_mat = requests.get(mat_link)
request_sta = requests.get(sta_link)

# Make BeautifulSoup objects for each of the course subjects
csc_soup = BeautifulSoup(request_csc.text, 'html.parser')
mat_soup = BeautifulSoup(request_mat.text, 'html.parser')
sta_soup = BeautifulSoup(request_sta.text, 'html.parser')


def Output_Text_Data(s1: BeautifulSoup, s2: BeautifulSoup, s3: BeautifulSoup) -> None:
    """
    Send the HTML data from the 3 BeautifulSoup objects and writes
    it to a textfile in a nicely formatted way
    """
    f = open("html_output", "w")
    f.write(s1.prettify + "\n")
    f.write(s2.prettify + "\n")
    f.write(s3.prettify + "\n")
    f.close

def Print_Text_Data(s1: BeautifulSoup, s2: BeautifulSoup, s3: BeautifulSoup) -> None:
    """
    Print the HTML data from the 3 BeautifulSoup objects
    in a prettyfied format to the console
    """
    print(csc_soup.prettify, "\n **END OF CSC**")
    print(mat_soup.prettify, "\n **END OF MAT**")
    print(sta_soup.prettify, "\n **END OF STA**\n")

if __name__ == "__main__":
    pass
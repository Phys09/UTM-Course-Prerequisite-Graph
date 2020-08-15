import requests  # get the html from websites
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
csc_soup = BeautifulSoup(request_csc.text, 'html.parser')
mat_soup = BeautifulSoup(request_mat.text, 'html.parser')
sta_soup = BeautifulSoup(request_sta.text, 'html.parser')



def Output_Text_Data(
    s1: BeautifulSoup,
    s2: BeautifulSoup,
    s3: BeautifulSoup
        ) -> None:
    """
    Send the HTML data from the 3 BeautifulSoup objects and writes
    it to a textfile in a nicely formatted way
    """
    # CSC HTML Output
    f = open("html_output_csc.html", "w")
    f.write(str(s1.prettify))
    f.write("\n")
    f.close

    # MAT HTML Output
    f = open("html_output_mat.html", "w")
    f.write(str(s2.prettify))
    f.write("\n")
    f.close

    # STA HTML Output
    f = open("html_output_sta.html", "w")
    f.write(str(s3.prettify))
    f.write("\n")
    f.close
    f.close


def Print_Text_Data(s1: BeautifulSoup, s2: BeautifulSoup, s3: BeautifulSoup) -> None:
    """
    Print the HTML data from the 3 BeautifulSoup objects
    in a prettyfied format to the console
    """
    print(csc_soup.prettify, "\n **END OF CSC**")
    print(mat_soup.prettify, "\n **END OF MAT**")
    print(sta_soup.prettify, "\n **END OF STA**\n")


def Get_CSC_Titles():
    """
    Get a list of title strings for CSC courses
    """
    pass


def Get_CSC_Descriptions():
    """
    Get a list of description strings for CSC courses.
    This descriptions are in order with that of the title list
    """


def Get_CSC_Prerequisites():
    """
    Get a list of course prerequisite lists.
    The index that points to each list of course prerequisites
    correspond with the title index, and descriptions.
    """


# MAT Section


def Get_MAT_Titles():
    """
    Get a list of title strings for MAT courses
    """
    pass


def Get_MAT_Descriptions():
    """
    Get a list of description strings for MAT courses.
    This descriptions are in order with that of the title list
    """

def Get_MAT_Prerequisites():
    """
    Get a list of course prerequisite lists.
    The index that points to each list of course prerequisites
    correspond with the title index, and descriptions.
    """


# STA Section


def Get_STA_Titles():
    """
    Get a list of title strings for STA courses
    """
    pass


def Get_STA_Descriptions():
    """
    Get a list of description strings for STA courses.
    This descriptions are in order with that of the title list
    """


def Get_STA_Prerequisites():
    """
    Get a list of course prerequisite lists.
    The index that points to each list of course prerequisites
    correspond with the title index, and descriptions.
    """


if __name__ == "__main__":
    # First, we output the data to the file
    Output_Text_Data(csc_soup, mat_soup, sta_soup)
    # Print_Text_Data(csc_soup, mat_soup, sta_soup)

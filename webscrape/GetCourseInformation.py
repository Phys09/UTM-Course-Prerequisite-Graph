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
csc_soup = BeautifulSoup(request_csc.text, html_parser)
mat_soup = BeautifulSoup(request_mat.text, html_parser)
sta_soup = BeautifulSoup(request_sta.text, html_parser)


def Output_HTML_Data(
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


def Print_Text_Data(
    s1: BeautifulSoup,
    s2: BeautifulSoup,
    s3: BeautifulSoup
        ) -> None:
    """
    Print the HTML data from the 3 BeautifulSoup objects
    in a prettyfied format to the console
    """
    print(csc_soup.prettify, "\n **END OF CSC**")
    print(mat_soup.prettify, "\n **END OF MAT**")
    print(sta_soup.prettify, "\n **END OF STA**\n")


# Get titles as a result set
csc_title_result_set = csc_soup.find_all('p', attrs={'class': 'titlestyle'})
mat_title_result_set = mat_soup.find_all('p', attrs={'class': 'titlestyle'})
sta_title_result_set = sta_soup.find_all('p', attrs={'class': 'titlestyle'})

# Get course descriptions as a result set
csc_desc_result_set = csc_soup.find_all('p', attrs={'span': 'normaltext'})
mat_desc_result_set = mat_soup.find_all('p', attrs={'span': 'normaltext'})
sta_desc_result_set = sta_soup.find_all('p', attrs={'span': 'normaltext'})


def write_csc_titles():
    """
    Simply iterate and print out the result of the csc title
    """
    f = open("csc_title_set_output.txt", "w")
    for tag_data in csc_title_result_set:
        f.write(str(tag_data.text) + ",\n")
    f.close


def write_mat_titles():
    """
    Simply iterate and print out the result of the mat title
    """
    f = open("mat_title_set_output.txt", "w")
    f.write(str(mat_title_result_set[:]))
    f.close


def write_sta_titles():
    """
    Simply iterate and print out the result of the sta title
    """
    f = open("sta_title_set_output.txt", "w")
    f.write(str(sta_title_result_set[:]))
    f.close


if __name__ == "__main__":
    # First, we output the data to the file
    Output_HTML_Data(csc_soup, mat_soup, sta_soup)
    write_csc_titles()
    write_mat_titles()
    write_sta_titles()
    # Print_Text_Data(csc_soup, mat_soup, sta_soup)

import requests  # get the html from websites
from bs4 import BeautifulSoup

def Output_HTML_Data(
    s1: BeautifulSoup,
    s2: BeautifulSoup,
    s3: BeautifulSoup
        ) -> None:
    """
    Send the HTML data from the 3 BeautifulSoup objects and writes
    it to a textfile in a nicely formatted way
    """
    def Output_CSC_HTML(b: BeautifulSoup):
        """
        Output the CSC HTML data to a file
        """
        # CSC HTML Output
        f = open("html_output_csc.html", "w")
        f.write(str(b.prettify))
        f.write("\n")
        f.close

    def Output_MAT_HTML(b: BeautifulSoup):
        """
        Output the MAT HTML data to a file
        """

        f = open("html_output_mat.html", "w")
        f.write(str(b.prettify))
        f.write("\n")
        f.close

    def Output_STA_HTML(b: BeautifulSoup):
        """
        Output the STA HTML data to a file
        """
        f = open("html_output_sta.html", "w")
        f.write(str(b.prettify))
        f.write("\n")
        f.close

    Output_CSC_HTML(s1)
    Output_MAT_HTML(s2)
    Output_STA_HTML(s3)


def write_set_data(result_set, subject: str, kind: str):
    """
    Iterate and print out the result of the result_ser data

    :result_set: a result set from beautifulsoup4

    :subject: string that determines subject we're working with
    
    :kind: string that determines type of data that result_set holds (title, description, etc...)
    
    """
    file_name = subject + "_" + kind + "_set_output.txt"
    f = open(file_name, "w")
    for tag_data in result_set:
        f.write(str(tag_data.text) + ",\n")
    f.close

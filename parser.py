from bs4 import BeautifulSoup
from request import Request


UNIVERSITY_LIST_URL = "https://yokatlas.yok.gov.tr/lisans-bolum.php?b=10024"
UNIVERSITY_BASE_URL = "https://yokatlas.yok.gov.tr/"


class Parser:
    def __init__(self):
        self.request = Request()

    def get_html(self, url):
        response = self.request.simple_get(url)
        return BeautifulSoup(response.text, "lxml")

    def parse_html(self, url):
        soup = self.get_html(url)
        university_divs = (soup.find_all(class_="panel panel-primary"))
        for div in university_divs:
            a = div.find("a")
            # todo: concetanate with base url and send request to related links -> last student's order
            # todo: from last element, get average nets
            # todo: find relation between nets and orders and plot
            #print(a.attrs["href"])
        #print(html)


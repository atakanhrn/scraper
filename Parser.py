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
        university_links = []
        average_nets_link = ""
        for div in university_divs:
            a = div.find("a")
            if university_divs.index(div) < (len(university_divs) - 1):
                university_links.append(UNIVERSITY_BASE_URL + a.attrs["href"])  ## except last element
            else:       ##last element
                average_nets_link = UNIVERSITY_BASE_URL + a.attrs["href"]


            #print(a.attrs["href"])
        return university_links, average_nets_link


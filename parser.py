from bs4 import BeautifulSoup
from request import Request


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
            #print(a)
            print(a.attrs["href"])
        #print(html)


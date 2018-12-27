from bs4 import BeautifulSoup
from request import Request


class Parser:
    def __init__(self):
        self.request = Request()

    def get_html(self, url):
        response = self.request.simple_get(url)
        if response is not None:
            return BeautifulSoup(response, "html.parser")
        else:
            print("Response error")

    def parse_html(self, url):
        html = self.get_html(url)
        university_divs = (html.find_all(class_ = "panel panel-primary", href = True))
        for div in university_divs:
            a = div.select("a")
            print(a)
        #print(html)


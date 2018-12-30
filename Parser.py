from bs4 import BeautifulSoup
from request import Request
from selenium import webdriver
from read import read_json
import time

UNIVERSITY_LIST_URL = "https://yokatlas.yok.gov.tr/2017/lisans-bolum.php?b=10024"
UNIVERSITY_BASE_URL = "https://yokatlas.yok.gov.tr/2017/"


class Parser:
    def __init__(self):
        self.request = Request()

    def get_html(self, url):
        response = self.request.simple_get(url)
        return BeautifulSoup(response.text, "lxml")

    def get_html_for_nets(self, url):
        browser = webdriver.PhantomJS()
        browser.get(url)
        self.click_button_with_id(browser, "h1210a")
        self.click_button_with_id(browser, "headingOne")
        self.click_button_with_id(browser, "h1070")
        time.sleep(5)
        return BeautifulSoup(browser.page_source, "lxml")

    def click_button_with_id(self, browser, id):
        button = browser.find_element_by_id(id)
        button.find_element_by_class_name("accordion-toggle").click()

    def get_university_urls(self, url):
        soup = self.get_html(url)
        university_divs = (soup.find_all(class_="panel panel-primary"))
        university_links = []
        average_nets_link = ""
        for div in university_divs:
            a = div.find("a")
            if university_divs.index(div) < (len(university_divs) - 1):
                university_links.append(UNIVERSITY_BASE_URL + a.attrs["href"])  ## except last element
        return university_links


    def get_math_net(self, soup):
        average_table_div = (soup.find(id="icerik_1210a"))
        average_table_rows = average_table_div.find_all(class_="text-center")
        if len(average_table_rows) > 8:
            return float(average_table_rows[8].text.replace(",", "."))
        else:
            return -1

    def get_order(self, soup):
        order_table_div = (soup.find(id="icerik_1070"))
        order_table_rows = order_table_div.find_all(align="center")
        if len(order_table_rows) > 5:
            if order_table_rows[5].text == "":
                return -1
            else:
                return int(order_table_rows[5].text.replace(".", ""))
        else:
            return -1

    def get_city(self, soup):
        city_header = soup.find("h3")
        university_text = city_header.text
        return university_text[university_text.find("(") + 1:university_text.find(")")]

    def get_region(self, city):
        data = (read_json("il-ilce.json"))
        for d in data:
            if d["il"] == city:
                return d["bolge"]

                
    def get_quota(self, soup):
        quota_table_div = (soup.find(id="icerik_1000_1"))
        quota_table_rows = quota_table_div.find_all(class_="text-center")
        if len(quota_table_rows) > 9:
            return int(quota_table_rows[9].text)
        else:
            return -1

    def parse_average_nets_and_order_from(self, url):
        soup = self.get_html_for_nets(url)
        average_net = self.get_math_net(soup)
        order = self.get_order(soup)
        quota = self.get_quota(soup)
        city = self.get_city(soup)
        region = self.get_region(city)
        return average_net, order, region, quota

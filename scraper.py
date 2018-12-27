from parser import Parser


UNIVERSITY_LIST_URL = "https://yokatlas.yok.gov.tr/lisans-bolum.php?b=10024"
if __name__ == '__main__':
    parser = Parser()
    parser.parse_html(UNIVERSITY_LIST_URL)
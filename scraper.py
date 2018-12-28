import Parser


if __name__ == '__main__':
    parser = Parser.Parser()
    university_links, average_nets_link = parser.parse_html(Parser.UNIVERSITY_LIST_URL)
    print(average_nets_link)
    # todo: get student order and average nets from links
    # todo: find relation between nets and orders and plot

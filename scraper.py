import Parser




if __name__ == '__main__':
    parser = Parser.Parser()
    university_urls = parser.get_university_urls(Parser.UNIVERSITY_LIST_URL)
    average_nets = []
    orders = []
    counter = 0
    f = open("average_and_orders_7.txt", "w+")
    for i in range(258, len(university_urls)):
        print(university_urls[i])
        print(counter)
        counter += 1
        average_net, order, region, quota = parser.parse_average_nets_and_order_from(university_urls[i])
        average_nets.append(average_net)
        orders.append(order)

        f.write(str(average_net) + "\t" + str(order) + "\t" + region + "\t" + str(quota) + "\n")
    f.close()
    # print(parser.parse_average_nets(average_nets_url))
    # todo: find relation between nets and orders and plot



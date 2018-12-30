import Parser
from read import read_txt
from Process_data import Process_data


if __name__ == '__main__':
    # university_parser("average_order_region_quota.txt")
    key_value_array = read_txt("average_and_orders_1.txt")
    process_data = Process_data(key_value_array)
    region_quota_dict = process_data.process_quotas()
    process_data.process_average_nets_and_orders()


def university_parser(file_name):
    parser = Parser.Parser()
    university_urls = parser.get_university_urls(Parser.UNIVERSITY_LIST_URL)
    f = open(file_name, "w+")
    for i in range(0, len(university_urls)):
        average_net, order, region, quota = parser.parse_average_nets_and_order_from(university_urls[i])

        f.write(str(average_net) + "\t" + str(order) + "\t" + region + "\t" + str(quota) + "\n")
    f.close()

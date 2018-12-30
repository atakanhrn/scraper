from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import numpy as np


class Process_data:
    def __init__(self, key_value_array):
        self.key_value_array = key_value_array
        return

    def calculate_r_square(self, orders, predicted_orders):
        return r2_score(orders, predicted_orders)

    def collect_region_quotas(self):
        region_quota_dict ={ "MARMARA" : [], "AKDENİZ" : [], "EGE" : [], "KARADENİZ" : [], "İÇ ANADOLU" : [], "GÜNEYDOĞU ANADOLU" : [], "DOĞU ANADOLU" : [], "KKTC": [], "YURTDIŞI": [] }
        region_university_count_dict ={ "MARMARA" : 0, "AKDENİZ" : 0, "EGE" : 0, "KARADENİZ" : 0, "İÇ ANADOLU" : 0, "GÜNEYDOĞU ANADOLU" : 0, "DOĞU ANADOLU" : 0, "KKTC": 0, "YURTDIŞI": 0 }
        for element in self.key_value_array:
            quota = int(element["quota"])
            region = element["region"]
            region_quota_dict[region].append(quota)
        return region_quota_dict

    def process_quotas(self):
        region_quota_dict = self.collect_region_quotas()
        # basic plot
        data = list(region_quota_dict.values())
        print(data)

        plt.boxplot(data, labels=list(region_quota_dict.keys()))
        plt.show()
    def get_average_nets_and_orders(self):
        average_nets = []
        orders = []
        for element in self.key_value_array:
            if element["average_net"] == "-1" or element["order"] == "-1":
                continue
            average_nets.append(float(element["average_net"]))
            orders.append(float(element["order"]))
        return average_nets, orders

    def test_func(self, average_nets, a, b):
        orders = []
        for net in average_nets:
            orders.append(a*net + b)
        return orders

    def process_average_nets_and_orders(self):
        average_nets, orders = self.get_average_nets_and_orders()
        fit_array = np.polyfit(average_nets, orders, 1)
        predicted_orders = self.test_func(average_nets, fit_array[0], fit_array[1])
        r_square_metric = self.calculate_r_square(orders, predicted_orders)
        print(r_square_metric)
        plt.plot(average_nets, predicted_orders, label='Fitted function', color="red")
        plt.scatter(average_nets, orders)
        plt.show()

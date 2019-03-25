""" Created by Oleksandr Sorocynskyi """
""" On 25/03/2019 """

from data import get_stock_history_sample

if __name__ == "__main__":
    res = get_stock_history_sample(100)
    print(res)
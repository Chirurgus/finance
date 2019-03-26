""" Created by Oleksandr Sorocynskyi """
""" On 25/03/2019 """

from random import sample

from iexdata import symbols, stock_history_daily

if __name__ == "__main__":
    all_symbols = symbols()
    history = stock_history_daily(sample(all_symbols, 100))
    history.to_csv(r'stock_history.csv')
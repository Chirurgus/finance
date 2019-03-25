""" Created by Oleksandr Sorocynskyi """
""" On 24/03/2019 """

from random import sample

from .api import symbols, stock_history

# Helper functions so that we don't need to make multiple calls form R
def get_stock_history_sample(num_stocks):
    all_symbols = symbols()
    return(stock_history(sample(all_symbols, num_stocks)))

__all__ =  ['symbols', 'stock_history']
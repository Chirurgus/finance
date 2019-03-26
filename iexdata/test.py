""" Created by Oleksandr Sorocynskyi """
""" On 25/03/2019 """

from unittest import TestCase

import pandas as pd

from . import symbols, stock_history_daily

class TestStockPriceHistory(TestCase):
    symbols = ["AAPL", "TSLA"]
    expected_num_col = 7
    expected_num_row_per_symbol = 1258 # 251.6 trading days/year

    def test_symbols_type(self):
        all_symbols = symbols()
        self.assertIsInstance(all_symbols, list)
    
    def test_stock_history_type(self):
        history = stock_history_daily(self.symbols)
        self.assertIsInstance(history, pd.DataFrame)

    def test_stock_history_col_count(self):
        history = stock_history_daily(self.symbols)
        self.assertEqual(len(history.columns), self.expected_num_col)

    def test_stock_history_row_count(self):
        history = stock_history_daily(self.symbols)
        self.assertEqual(len(history.index),
                         self.expected_num_row_per_symbol*len(self.symbols))
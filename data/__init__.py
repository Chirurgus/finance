""" Created by Oleksandr Sorocynskyi """
""" On 24/03/2019 """

from random import sample
from datetime import datetime

import pandas as pd 

import iexfinance as iex

NUM_ASSETS = 100

def get_stock_history():
    symbols_all = iex.refdata.get_symbols()

    # Il en a 8721 en tout
    num_assets = min(NUM_ASSETS, len(symbols_all))

    symbols_sample = [ s['symbol'] for s in sample(symbols_all, num_assets) ]

    # 5 years of data
    start_date = datetime(2014, 3, 23)
    end_date = datetime(2019, 3, 23)
    price_history_multicol = iex.stocks.get_historical_data(
                                            symbols_sample,
                                            start_date,
                                            end_date,
                                            output_format='pandas'
                                            )
    # makes date a column
    price_history_multicol.reset_index(inplace=True)

    price_history_flat = pd.DataFrame()
    for symbol in symbols_sample:
        df = pd.concat(
            [ price_history_multicol[col] for col in [symbol, 'date'] ],
            axis=1
            )
        df['symbol'] = symbol
        price_history_flat = price_history_flat.append(df)
    
    return(price_history_flat)

__all__ =  ['get_stock_history']

if __name__ == "__main__":
    x = get_stock_history()
    x.isnull.sum()[0]
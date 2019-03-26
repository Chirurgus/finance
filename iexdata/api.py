""" Created by Oleksandr Sorocynskyi """
""" On 25/03/2019 """

from datetime import datetime

import pandas as pd 

import iexfinance as iex

def symbols():
    symbols_all = iex.refdata.get_symbols()
    return([ s['symbol'] for s in symbols_all])

def stock_history_daily(symbols):
    # 5 years of data
    start_date = datetime(2014, 3, 23)
    end_date = datetime(2019, 3, 23)
    price_history_multicol = iex.stocks.get_historical_data(
                                            symbols,
                                            start_date,
                                            end_date,
                                            output_format='pandas'
                                            )
    # makes date a column
    price_history_multicol.reset_index(inplace=True)

    price_history_flat = pd.DataFrame()
    for symbol in symbols:
        df = pd.concat(
            [ price_history_multicol[col] for col in [symbol, 'date'] ],
            axis=1
            )
        df['symbol'] = symbol
        price_history_flat = price_history_flat.append(df)
    
    return(price_history_flat)
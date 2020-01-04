import yfinance as yf
import pandas as panda


def load_yahoo_quote(ticker, begindate, enddate):
    ticker = yf.Ticker(ticker)
    df = panda.DataFrame(ticker.history(start=begindate, end=enddate,actions=False))
    close_prices = df.get('Close').tolist()
    timestamps = df.index.tolist()
    dates = list(map(lambda timestamp: timestamp.date().strftime("%d-%m-%Y"), timestamps))
    if len(dates) == 0 or len(close_prices) == 0:
        raise Exception("Ei leidnud väärtpaberit!")
    return close_prices, dates

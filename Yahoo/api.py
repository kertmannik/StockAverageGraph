import yfinance as yf
import pandas as panda


def load_yahoo_quote(ticker, begindate, enddate):
    ticker = yf.Ticker(ticker)
    df = panda.DataFrame(ticker.history(start=begindate, end=enddate,actions=False))
    close_prices = df.get('Close').tolist()
    timestamps = df.index.tolist()
    dates = []
    for timestamp in timestamps:
        dates.append(timestamp.date().strftime("%d-%m-%Y"))
    return close_prices, dates

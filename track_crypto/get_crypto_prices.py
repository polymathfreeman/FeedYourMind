import pandas_datareader as web
import matplotlib.pyplot as plt
import mplfinance as mpf
import seaborn as sns
import datetime as dt

currency = "USD"
metric = "Close"

start = dt.datetime(2020, 1, 1)
end = dt.datetime.now()

crypto = ['BTC', 'ETH', 'ADA', 'SOL', 'DOT',
         'MATIC', 'TRX', 'WBTC', 'AVAX', 'UNI']
#,
#           'MATIC', 'TRX', 'WBTC', 'AVAX', 'UNI',
#           'LINK', 'ATOM', 'XLM', 'CRO', 'APE']
#crypto = ['BTC', 'ETH', 'LTC', 'XRP', 'DASH', 'SC']
colnames = []

first = True

for ticker in crypto:
    data = web.DataReader(f'{ticker}-{currency}', "yahoo", start, end)
    if first:
        combined = data[[metric]].copy()
        colnames.append(ticker)
        combined.columns = colnames
        first = False
    else:
        combined = combined.join(data[metric])
        colnames.append(ticker)
        combined.columns = colnames

plt.yscale('log')

for ticker in crypto:
    plt.plot(combined[ticker], label=ticker)

plt.legend(loc="upper right")

plt.show()

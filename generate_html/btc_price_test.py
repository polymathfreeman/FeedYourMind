from bitcoin_value import currency
from coingecko import CoinGecko

btc_usd = currency("USD")
btc_eur = currency("EUR")

cg = CoinGecko()
btc = cg.get_simple_price(ids=["bitcoin"], vs_currencies=["usd", "eur"])

for curr in ["usd", "eur"]:
    print(f"From Coingecko: 1 BTC = {btc['bitcoin'][curr]} {curr.upper()}")
    check = "https://www.coingecko.com/"
    print(f"Check yourself: {check}")
    input("Do you know arbitrage? ")
    random_price = currency(curr.upper())
    print(f"From somewhere else: 1 BTC = {random_price} {curr.upper()}")




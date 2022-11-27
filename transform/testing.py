import yfinance as yf 

def financials():
    conversion=yf.download('ETH-USD', start='2022-11-01', end='2022-11-26')
    print(conversion)


financials() 



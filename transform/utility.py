import pandas as pd 
import yfinance as yf 
import requests

class Crypto():

    def __init__(self, parameters):

        self.parameters = parameters
        self.base = 'https://api.x.immutable.com/v1/'
        self.cursor = ""

        while True:
            data = self.get_main_request()
            if data['remaining'] == 1 : # means there are more results to query 
                self.get_main_request()
                self.json_elements(data)
                self.cursor = self.cursor_helper(data)

            else:
                break 
        
        if self.endpoint in ['mints', 'transfers', 'deposits', 'withdrawals']:
            self.df = pd.DataFrame(self.json_elements(data)) 
            self.df.columns = self.df.columns.str.upper() 
        else:
            self.df = pd.DataFrame(self.json_elements(data)) 
            conversion_rate = self.financials()
            self.df['daily_avg_value'] = self.df['updated_timestamp'].map(conversion_rate)
            self.df.columns=self.df.columns.str.upper()

    def get_main_request(self): 
        session = requests.get(url=f'{self.base}{self.endpoint}?cursor={self.cursor}', params=self.parameters)
        session.raise_for_status()
        return session.json()

    def cursor_helper(self, data):
        return data['cursor']

    def financials(self):
        conversion=yf.download(tickers="ETH-USD", start=self.yesterday, end=self.today)
        avg_daily_value = (conversion['High'] + conversion['Low']) /2
        return avg_daily_value


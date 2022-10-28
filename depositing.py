import requests
import pandas as pd 


class MoneyIn:
    
    def __init__(self, parameters):
        self.parameters = parameters
        self.base = 'https://api.x.immutable.com/v1/'
        self.deposit_endpoint = 'deposits'
        self.cursor = ""
        self.deposits = []
        self.df = None

        while True:
            data = self.get_main_request()
            if data['remaining'] == 1 :
                self.get_main_request()
                self.json_elements(data)
                self.cursor = self.cursor_helper(data)

            else:
                break 

        self.df = pd.DataFrame(self.json_elements(data)) 
        self.df.columns = self.df.columns.str.upper() 


    def get_main_request(self): 
        session = requests.get(url=f'{self.base}{self.deposit_endpoint}?cursor={self.cursor}', params=self.parameters)
        session.raise_for_status()
        return session.json()
    

    def json_elements(self, data):
        for element in data['result']:
            timestamp = element['timestamp'].split('T')[0]
            user = element['user'] 
            currency = element['token']['type'] 
            token_address = element['token']['data']['token_address'] 
            quantity = float(element['token']['data']['quantity']) / 10 ** float(element['token']['data']['decimals'])

            deposit = {
                'timestamp' : timestamp ,
                'user': user, 
                'currency': currency,
                'token_address': token_address, 
                'quantity': quantity
            }
            
            self.deposits.append(deposit)
        return self.deposits 


    def cursor_helper(self, data):
        return data['cursor']






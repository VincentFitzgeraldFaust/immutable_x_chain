import requests
import pandas as pd 


class Withdraw:

    def __init__(self, parameters):
        self.base = 'https://api.x.immutable.com/v1/'
        self.withdraw_endpoint = 'withdrawals'
        self.cursor = ""
        self.withdrawals = []
        self.parameters = parameters
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
        session = requests.get(url=f'{self.base}{self.withdraw_endpoint}?cursor={self.cursor}', params=self.parameters)
        session.raise_for_status()
        return session.json()


    def json_elements(self, data):
        for element in data['result']:
            transaction_id = element['transaction_id']
            timestamp = element['timestamp'].split('T')[0]
            withdraw_status = element['withdrawn_to_wallet']
            user = element['sender'] 
            currency = element['token']['type'] 
            quantity = float(element['token']['data']['quantity']) / 10 ** float(element['token']['data']['decimals'])
            token_address = element['token']['data']['token_address']

            withdrawer = {
            'timestamp' : timestamp ,
            'transaction_id' : transaction_id,
            'timestamp' : timestamp,
            'withdraw_status' : withdraw_status, 
            'user' : user, 
            'currency' : currency, 
            'quantity' : quantity, 
            'token_address' : token_address
        }
        
            self.withdrawals.append(withdrawer)
        return self.withdrawals


    def cursor_helper(self, data):
        return data['cursor']
    






    
    

        











import requests
from utility import Crypto



class Deposit(Crypto):
    
    def __init__(self, parameters):
        self.deposit_endpoint = 'deposits'
        self.deposits = []
        super().__init__(parameters)

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

            depositer = {
                'timestamp' : timestamp ,
                'user': user, 
                'currency': currency,
                'token_address': token_address, 
                'quantity': quantity
            }
            
            self.deposits.append(depositer)
        return self.deposits 








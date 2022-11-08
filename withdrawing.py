import requests
from utility import Crypto


class Withdraw(Crypto):

    def __init__(self, parameters):
        self.endpoint = 'withdrawals'
        self.withdrawals = []
        super().__init__(parameters)

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


 
    






    
    

        











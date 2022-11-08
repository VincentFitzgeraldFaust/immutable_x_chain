import requests
from utility import Crypto


class Mint(Crypto):

    def __init__(self,parameters):
        self.endpoint = 'mints'
        self.mints = []
        super().__init__(parameters)

    def json_elements(self, data):
        for element in data['result']:
            transaction_id = element['transaction_id']
            timestamp = element['timestamp'].split('T')[0]
            user = element['user'] 
            currency = element['token']['type'] 
            token_address = element['token']['data']['token_address'] 

            minter = {
                'transaction_id' : transaction_id, 
                'timestamp' : timestamp ,
                'user': user, 
                'currency': currency,
                'token_address': token_address, 
            }
            
            self.mints.append(minter)
        return self.mints



    

        

        


        











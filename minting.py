import requests
import pandas as pd 


class Creation:

    def __init__(self,parameters):
        self.parameters = parameters
        self.base = 'https://api.x.immutable.com/v1/'
        self.mint_endpoint = 'mints'
        self.cursor = ""
        self.mints = []
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
        session = requests.get(url=f'{self.base}{self.mint_endpoint}?cursor={self.cursor}', params=self.parameters)
        session.raise_for_status()
        return session.json()


    def json_elements(self, data):
        for element in data['result']:
            transaction_id = element['transaction_id']
            timestamp = element['timestamp'].split('T')[0]
            user = element['user'] 
            currency = element['token']['type'] 
            token_address = element['token']['data']['token_address'] 

            mint = {
                'transaction_id' : transaction_id, 
                'timestamp' : timestamp ,
                'user': user, 
                'currency': currency,
                'token_address': token_address, 
            }
            
            self.mints.append(mint)
        return self.mints


    def cursor_helper(self, data):
        return data['cursor']

    

        

        


        











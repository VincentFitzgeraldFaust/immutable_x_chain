from utility import Crypto



class Deposit(Crypto):
    
    def __init__(self, parameters, today, yesterday):
        self.endpoint = 'deposits'
        self.deposits = []
        self.today = today
        self.yesterday = yesterday
        super().__init__(parameters)
    
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








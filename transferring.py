from utility import Crypto


class Transfer(Crypto):

    def __init__(self,parameters):
        self.endpoint = 'transfers'
        self.transfers = []
        super().__init__(parameters)

    def json_elements(self, data):
        for element in data['result']:
            transaction_id = element['transaction_id']
            timestamp = element['timestamp'].split('T')[0]
            user = element['user']
            receiver = element['receiver']
            token_type = element['token']['type']
            token_address = element['token']['data']['token_address']
            quantity = float(element['token']['data']['quantity']) /  10 ** float(element['token']['data']['decimals'])

            transferer = {
                'timestamp' : timestamp ,
                'transaction_id' : transaction_id,
                'user' : user, 
                'receiver' : receiver, 
                'token_type' : token_type, 
                'token_address' : token_address, 
                'quantity' : quantity         
            }
            
            self.transfers.append(transferer)
        return self.transfers


    

        











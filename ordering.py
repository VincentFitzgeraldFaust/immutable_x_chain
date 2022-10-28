
import requests
import pandas as pd


class OrderUp:
    
    def __init__(self, parameters):
        self.parameters = parameters
        self.base = 'https://api.x.immutable.com/v1/'
        self.deposit_endpoint = 'orders'
        self.cursor = ""
        self.orders = []
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
            order_id = element['order_id']
            user = element['user'] 
            sell_type = element['sell']['type']
            sell_token_address = element['sell']['data']['token_address']
            sell_quantity = float(element['sell']['data']['quantity'])
            buy_type = element['buy']['type']
            buy_token_address= element['buy']['data']['token_address']
            buy_quantity = float(element['buy']['data']['quantity']) 
           
        if element['sell']['type'] == 'ETH' or element['sell']['type'] == 'ERC20':
            sell_quantity = float(element['sell']['data']['quantity']) / 10 ** float(element['sell']['data']['decimals'])
            sell_quantity = f'{sell_quantity:.18f}'
        else:
            sell_quantity = element['sell']['data']['quantity']

        if element['buy']['type'] == 'ETH' or element['buy']['type'] == 'ERC20':  
            buy_quantity = float(element['buy']['data']['quantity']) / 10 ** float(element['buy']['data']['decimals'])
            buy_quantity = f'{buy_quantity:.18f}'
        else:
            buy_quantity = element['buy']['data']['quantity']
        
        order = {
            'timestamp' : timestamp ,
            'order_id' : order_id,
            'user': user, 
            'sell_type' : sell_type, 
            'sell_token_address' : sell_token_address, 
            'sell_quantity' : sell_quantity, 
            'buy_type' : buy_type, 
            'buy_token_address' : buy_token_address, 
            'buy_quantity' : buy_quantity
        }
        
        self.orders.append(order)
        return self.orders


    def cursor_helper(self, data):
        return data['cursor']



                        

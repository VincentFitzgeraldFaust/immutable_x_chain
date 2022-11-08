from utility import Crypto


class Order(Crypto):
    
    def __init__(self, parameters):
        self.endpoint = 'orders'
        self.orders = []
        super().__init__(parameters)

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
        
        orderer = {
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
        
        self.orders.append(orderer)
        return self.orders





                        

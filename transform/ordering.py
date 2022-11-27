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
            sell_image_url = element['sell']['data']['properties']['image_url']
            buy_type = element['buy']['type']
            buy_token_address= element['buy']['data']['token_address']
            buy_quantity = float(element['buy']['data']['quantity']) / 10 ** float(element['buy']['data']['decimals'])
        
            orderer = {
                'timestamp' : timestamp ,
                'order_id' : order_id,
                'user': user, 
                'sell_type' : sell_type, 
                'sell_token_address' : sell_token_address, 
                'sell_quantity' : sell_quantity, 
                'sell_image_url' : sell_image_url, 
                'buy_type' : buy_type, 
                'buy_token_address' : buy_token_address, 
                'buy_quantity' : buy_quantity
            }
            
            self.orders.append(orderer)
        return self.orders





                        

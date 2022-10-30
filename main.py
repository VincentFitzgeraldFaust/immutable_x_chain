import datetime 

from depositing import MoneyIn
from withdrawing import MoneyOut
from minting import Creation
from transferring import Transference
from ordering import OrderUp


def main():

    today = datetime.datetime.utcnow()
    yesterday = today - datetime.timedelta(days=1) 
    today = today.strftime('%Y-%m-%d')
    yesterday = yesterday.strftime('%Y-%m-%d') 

    #creating objects across deposits, withdrawals, mints, transfer and orders endpoints respectively 
    
    money_in = MoneyIn(parameters = {'min_timestamp' : f'{yesterday}T00:00:00.00Z', 
                                     'max_timestamp' : f'{yesterday}T23:59:59.99Z',
                                     'direction' : 'asc'})

    money_out = MoneyOut(parameters = {'min_timestamp' : f'{yesterday}T00:00:00.00Z', 
                                     'max_timestamp' : f'{yesterday}T23:59:59.99Z',
                                     'direction' : 'asc'})

    gods_creates = Creation(parameters = {'min_timestamp' : f'{yesterday}T00:00:00.00Z', 
                                     'max_timestamp' : f'{yesterday}T23:59:59.99Z',
                                     'token_address' : '0xacb3c6a43d15b907e8433077b6d38ae40936fe2c', 
                                     'direction' : 'asc'})
    
    gods_moves = Transference(parameters = {'min_timestamp' : f'{yesterday}T00:00:00.00Z', 
                                     'max_timestamp' : f'{yesterday}T23:59:59.99Z',
                                     'token_address' : '0xacb3c6a43d15b907e8433077b6d38ae40936fe2c',
                                     'direction' : 'asc'})
    
    gods_orders = OrderUp(parameters = {'min_timestamp' : f'{yesterday}T00:00:00.00Z', 
                                        'max_timestamp' : f'{yesterday}T23:59:59.99Z',
                                        'order_by' : 'timestamp', 
                                        'direction' : 'asc',
                                        'sell_token_address' : '0xacb3c6a43d15b907e8433077b6d38ae40936fe2c'
                                        })
    









if __name__ == '__main__':
    main()



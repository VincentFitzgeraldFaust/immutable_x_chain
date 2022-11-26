import datetime 

from depositing import Deposit
from withdrawing import Withdraw
from minting import Mint
from transferring import Transfer
from ordering import Order


def main():

    today = datetime.datetime.utcnow()
    yesterday = today - datetime.timedelta(days=1) 
    today = today.strftime('%Y-%m-%d')
    yesterday = yesterday.strftime('%Y-%m-%d') 

    #creating objects across deposits, withdrawals, mints, transfer and orders endpoints respectively 
    
    money_in = Deposit(parameters = {'min_timestamp' : f'{yesterday}T00:00:00.00Z', 
                                     'max_timestamp' : f'{yesterday}T23:59:59.99Z',
                                     'token_address' : '0x8cb332602d2f614b570c7631202e5bf4bb93f3f6', 
                                     'direction' : 'asc'})
        
    money_out = Withdraw(parameters = {'min_timestamp' : f'{yesterday}T00:00:00.00Z', 
                                     'max_timestamp' : f'{yesterday}T23:59:59.99Z',
                                     'token_address' : '0x8cb332602d2f614b570c7631202e5bf4bb93f3f6', 
                                     'direction' : 'asc'})
    
    hro_creates = Mint(parameters = {'min_timestamp' : f'{yesterday}T00:00:00.00Z', 
                                     'max_timestamp' : f'{yesterday}T23:59:59.99Z',
                                     'token_address' : '0x8cb332602d2f614b570c7631202e5bf4bb93f3f6', 
                                     'direction' : 'asc'})
    
    hro_moves = Transfer(parameters = {'min_timestamp' : f'{yesterday}T00:00:00.00Z', 
                                     'max_timestamp' : f'{yesterday}T23:59:59.99Z',
                                     'token_address' : '0x8cb332602d2f614b570c7631202e5bf4bb93f3f6',
                                     'direction' : 'asc'})
    
    hro_orders = Order(parameters = {'min_timestamp' : f'{yesterday}T00:00:00.00Z', 
                                        'max_timestamp' : f'{yesterday}T23:59:59.99Z',
                                        'order_by' : 'timestamp', 
                                        'direction' : 'asc',
                                        'sell_token_address' : '0x8cb332602d2f614b570c7631202e5bf4bb93f3f6'
                                        })
    
  
    print(money_in.df)   
    print(money_out.df)
    print(hro_creates.df)
    print(hro_moves.df)
    print(hro_orders.df)







if __name__ == '__main__':
    main()



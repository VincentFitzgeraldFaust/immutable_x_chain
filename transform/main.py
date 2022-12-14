import datetime

from depositing import Deposit
from minting import Mint
from ordering import Order
from transferring import Transfer
from withdrawing import Withdraw


def main():

    today = datetime.datetime.utcnow()
    yesterday = today - datetime.timedelta(days=1)
    today = today.strftime('%Y-%m-%d')
    yesterday = yesterday.strftime('%Y-%m-%d')

    # creating objects across deposits, withdrawals, mints, transfer and orders endpoints respectively

    hro_deposits = Deposit(parameters={'min_timestamp': f'{yesterday}T00:00:00.00Z',
                                       'max_timestamp': f'{yesterday}T23:59:59.99Z',
                                       'token_address': '0x8cb332602d2f614b570c7631202e5bf4bb93f3f6',
                                       'direction': 'asc'})

    hro_withdraws = Withdraw(parameters={'min_timestamp': f'{yesterday}T00:00:00.00Z',
                                         'max_timestamp': f'{yesterday}T23:59:59.99Z',
                                         'token_address': '0x8cb332602d2f614b570c7631202e5bf4bb93f3f6',
                                         'direction': 'asc'})

    hro_creates = Mint(parameters={'min_timestamp': f'{yesterday}T00:00:00.00Z',
                                   'max_timestamp': f'{yesterday}T23:59:59.99Z',
                                   'token_address': '0x8cb332602d2f614b570c7631202e5bf4bb93f3f6',
                                   'direction': 'asc'})

    hro_moves = Transfer(parameters={'min_timestamp': f'{yesterday}T00:00:00.00Z',
                                     'max_timestamp': f'{yesterday}T23:59:59.99Z',
                                     'token_address': '0x8cb332602d2f614b570c7631202e5bf4bb93f3f6',
                                     'direction': 'asc'})

    hro_orders = Order(parameters={'min_timestamp': f'{yesterday}T00:00:00.00Z',
                                   'max_timestamp': f'{yesterday}T23:59:59.99Z',
                                   'order_by': 'timestamp',
                                   'direction': 'asc',
                                   'sell_token_address': '0x8cb332602d2f614b570c7631202e5bf4bb93f3f6'
                                   },
                       today=today,
                       yesterday=yesterday)

    print(hro_deposits.df)
    print(hro_withdraws.df)
    print(hro_creates.df)
    print(hro_moves.df)
    print(hro_orders.df)


if __name__ == '__main__':
    main()

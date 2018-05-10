# bitbank-client

[![PyPI version](https://badge.fury.io/py/bitbank-client.svg)](https://badge.fury.io/py/bitbank-client)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

bitbank-client is a python client (sync/async) library for bitbank api

## Installation

    $ pip install bitbank-client

## Usage

```python
#
# sync
#
from bitbank_client.sync import Client

client = Clinet(public_key='your api key', private_key='your api secret')
response = client.get_ticker(pair='btc_jpy')
print(response.status_code, response.json())

#
# async
#
import grequests
from bitbank_client.async import Async

client = Async(public_key='your api key', private_key='your api secret')
reqs = [client.get_ticker(pair='btc_jpy'), client.get_depth(pair='btc_jpy'), ...]
response = grequests.map(reqs)
for r in response:
	print(r.status_code, r.json())


client.get_ticker(pair='btc_jpy') # GET /{pair}/ticker
client.get_depth(pair='btc_jpy') # GET /{pair}/depth
client.get_transactions(pair='btc_jpy') # GET /{pair}/transactions
client.get_transactions(pair='btc_jpy', yyyymmdd='20180509') # GET /{pair}/transactions/{YYYYMMDD}
client.get_candlestick(pair='btc_jpy', candle_type='1day', yyyymmdd='2018') # GET /{pair}/candlestick/{candle-type}/{YYYY}
client.get_candlestick(pair='btc_jpy', candle_type='1hour', yyyymmdd='20180510') # GET /{pair}/candlestick/{candle-type}/{YYYY}
client.get_assets() # GET /user/assets
client.get_order(pair='btc_jpy', order_id=1) # GET /user/spot/order
client.order(pair='btc_jpy', amount=1, price=1, side='buy', type='limit') # POST /user/spot/order
client.cancel_order(pair='btc_jpy', order_id=1) # POST /user/spot/cancel_order
client.cancel_orders(pair='btc_jpy', order_ids=[1,2]) # POST /user/spot/cancel_orders
client.orders_info(pair='btc_jpy', order_ids=[1,2]) # POST /user/spot/orders_info
client.get_active_orders(pair='btc_jpy') # GET /user/spot/active_orders
client.get_trade_history(pair='btc_jpy') # GET /user/spot/trade_history
client.get_withdrawal_account(asset='btc') # GET /user/withdrawal_account
client.request_withdrawal(asset='btc', uuid=1, amount=1) # POST /user/request_withdrawal
client.request_withdrawal(asset='btc', uuid=1, amount=1, otp_token='xxx') # POST /user/request_withdrawal
client.request_withdrawal(asset='btc', uuid=1, amount=1, sms_token='xxx') # POST /user/request_withdrawal
```

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request
# coding: utf-8
import hashlib
import requests
import time
import hmac
import json
import urllib

class Client(object):

	def __init__(self, **kwargs):
		self.public_origin = kwargs.get('public_origin', 'https://public.bitbank.cc')
		self.private_origin = kwargs.get('private_origin', 'https://api.bitbank.cc')
		self.public_key = kwargs.get('public_key', None)
		if self.public_key is None:
			raise Exception('api key is absent.')
		self.private_key = kwargs.get('private_key', None)
		if self.private_key is None:
			raise Exception('secret key is absent.')
		self.timeout = kwargs.get('timeout', None)

	def _requests_public(self, path):
		uri = self.public_origin + path
		res = requests.get(uri, timeout=self.timeout)

		return res

	def _requests_private(self, path, method='GET', params=None):
		nonce = str(time.time())
		if method == 'GET':
			text = nonce + path + urllib.parse.urlencode(params)
			uri = '{0}{1}{2}'.format(self.private_origin, path, urllib.parse.urlencode(params))
		else: #method == 'POST'
			text = nonce + json.dumps(params)
			uri = '{0}{1}'.format(self.private_origin, path)
		headers = {
			'ACCESS-KEY': self.public_key,
			'ACCESS-NONCE': nonce,
			'ACCESS-SIGNATURE': self._signature(text),
			'Content-Type': 'application/json'
			}
		if method == 'GET':
			res = requests.get(uri, headers=headers, timeout=self.timeout, params=params)
		else: #method == 'POST'
			res = requests.post(uri, headers=headers, timeout=self.timeout, data=params)

		return res

	def _signature(self, params):
		sign = hmac.new(self.private_key.encode('utf-8'), params.encode('utf-8'), hashlib.sha256).hexdigest()
		return sign

	def get_ticker(self, **kwargs):
		params = kwargs
		path = '/{0}/ticker'.format(params['pair'])

		data = self._requests_public(path)

		return data

	def get_depth(self, **kwargs):
		params = kwargs
		path = '/{0}/depth'.format(params['pair'])

		data = self._requests_public(path)

		return data

	def get_transactions(self, **kwargs):
		params = kwargs
		path = '/{0}/transactions'.format(params['pair'])
		yyyymmdd = params.get('yyyymmdd', None)
		if yyyymmdd is not None:
			path += '/{0}'.format(params['yyyymmdd'])

		data = self._requests_public(path)

		return data

	def get_candlestick(self, **kwargs):
		params = kwargs
		path = '/{0}/candlestick/{1}/{2}'.format(params['pair'], params['candle_type'], params['yyyymmdd'])

		data = self._requests_public(path)

		return data

	def get_assets(self, **kwargs):
		params = kwargs
		path = '/v1/user/assets'

		data = self._requests_private(path, params=params)

		return data

	def get_order(self, **kwargs):
		params = kwargs
		path = '/v1/user/spot/order'

		data = self._requests_private(path, params=params)

		return data

	def order(self, **kwargs):
		params = kwargs
		path = '/v1/user/spot/order'

		data = self._requests_private(path, method='POST', params=params)

		return data

	def cancel_order(self, **kwargs):
		params = kwargs
		path = '/v1/user/spot/cancel_order'

		data = self._requests_private(path, method='POST', params=params)

		return data

	def cancel_orders(self, **kwargs):
		params = kwargs
		path = '/v1/user/spot/cancel_orders'

		data = self._requests_private(path, method='POST', params=params)

		return data

	def orders_info(self, **kwargs):
		params = kwargs
		path = '/v1/user/spot/orders_info'

		data = self._requests_private(path, method='POST', params=params)

		return data

	def get_active_orders(self, **kwargs):
		params = kwargs
		path = '/v1/user/spot/active_orders'

		data = self._requests_private(path, params=params)

		return data

	def get_trade_history(self, **kwargs):
		params = kwargs
		path = '/v1/user/spot/trade_history'

		data = self._requests_private(path, params=params)

		return data

	def get_withdrawal_account(self, **kwargs):
		params = kwargs
		path = '/v1/user/withdrawal_account'

		data = self._requests_private(path, params=params)

		return data

	def request_withdrawal(self, **kwargs):
		params = kwargs
		path = '/v1/user/request_withdrawal'

		data = self._requests_private(path, method='POST', params=params)

		return data

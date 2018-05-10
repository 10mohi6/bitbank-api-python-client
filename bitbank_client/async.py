# coding: utf-8
import grequests
import time
import json
import urllib
from sync import Client

class Async(Client):

	def _requests_public(self, path):
		uri = self.public_origin + path
		res = grequests.get(uri, timeout=self.timeout)

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
			res = grequests.get(uri, headers=headers, timeout=self.timeout, params=params)
		else: #method == 'POST'
			res = grequests.post(uri, headers=headers, timeout=self.timeout, data=params)

		return res

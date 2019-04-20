'''
*Made for donations to Notre Dame <3
*Author: JonPizza @ Github, UserJonPizza#4510 @ Ravencoin Community Discord
'''

has_passphrase = True
your_passphrase = '' # If you have no passphrase set "has_passphrase" to "False" and leave this blank
your_wallet_address = ''
asset_name = '' # The asset you wish to transact
assets_per_rvn = 1 # For each RVN given, how many assets do you want to send out?
confirms = 5 # 5 should be minimum, 60 should garentee a 0 chance of a double spend

# Do not change anything below this line unless you know what you are doing!

import subprocess
import json
import time
import requests

base = './raven-cli'
raised = 0


def call(command):
	command = command.split(' ')
	proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	o, e = proc.communicate()
	output = o.decode('ascii')
	error = e.decode('ascii')

	return (output, error)

def txid_addr(txid):
	api_response = requests.get('https://ravencoin.network/api/tx/' + txid)
	x = json.loads(api_response.content.decode('utf-8'))

	return (x['vin'][0]['addr'], x['vin'][0]['value'])


class ravencoin:
	def __init__(self, passphrase, sender_addr):
		self.passphrase = passphrase
		self.sender_addr = sender_addr

	def unlock(self, timeout=600):
		call(f'{base} walletpassphrase {self.passphrase} {timeout}')

	def bal(self):
		bal = call(f'{base} getbalance')[0]
		return float(bal)

	def send_asset(self, asset, amount, reciver):
		call(f'{base} transfer {asset} {amount} {reciver}')

	def send_assets(self):
		c1 = call(f'{base} listunspent')
		l_c1 = json.loads(c1[0])
		txid_l = []

		for i in l_c1:
			if i['confirmations'] == confirms:
				txid_l.append(i['txid'])

		for i in txid_l:
			sdr = txid_addr(i)
			if sdr[0] != 'RQdE5WjsstVi3bZVURQ55XZjCcnsMJyZqq' and sdr[0] != 'RTraysiMMzReEQHKtGtgRtVdGjg4vRA36d':
				raised += sdr[1]
				self.send_asset(asset_name, float(sdr[1])*assets_per_rvn, sdr[0])
				print(f'{float(sdr[1])*assets_per_rvn} {asset_name} tokens(s) sent to {sdr[0]}! Total Raised: {raised}')


if __name__ == '__main__':
	rvn = ravencoin(your_passphrase, your_wallet_address)
	while True:
		if has_passphrase == True:
			rvn.unlock()
		rvn.send_assets()
		time.sleep(60)

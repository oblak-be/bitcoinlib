# -*- coding: utf-8 -*-
#
#    bitcoinlib - Compact Python Bitcoin Library
#    BlockCypher client
#    © 2016 November - 1200 Web Development <http://1200wd.com/>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from bitcoinlib.services.baseclient import BaseClient, ClientError

PROVIDERNAME = 'blockcypher'


class BlockCypher(BaseClient):

    def __init__(self, network):
        super(self.__class__, self).__init__(network, PROVIDERNAME)

    def compose_request(self, method, data, parameter='', variables=None):
        url_path = method + '/' + data
        if parameter:
            url_path += '/' + parameter
        return self.request(url_path, variables)

    def getbalance(self, addresslist):
        addresses = ';'.join(addresslist)
        res = self.compose_request('addrs', addresses, 'balance')
        if isinstance(res, dict):
            return float(res['final_balance'])
        else:
            balance = 0.0
            for rec in res:
                balance += float(rec['final_balance'])
            return balance * self.units

    def utxos(self, addresslist):
        addresses = ';'.join(addresslist)
        res = self.compose_request('addrs', addresses, variables=[('unspentOnly', 1)])
        utxos = []
        for a in res:
            address = a['address']
            if a['n_tx'] == 0:
                continue
            for utxo in a['txrefs']:
                utxos.append({
                    'address': address,
                    'tx_hash': utxo['tx_hash'],
                    'confirmations': utxo['confirmations'],
                    'output_n': utxo['tx_output_n'],
                    'index': 0,
                    'value': utxo['value'] * self.units,
                    'script': '',
                })
        return utxos

    def sendrawtransaction(self, rawtx):
        return self.compose_request('txs', 'push', variables=[('tx', rawtx)])

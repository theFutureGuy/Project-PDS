from web3 import Web3
import json


ganache_url="http://127.0.0.1:7545"
web3=Web3(Web3.HTTPProvider(ganache_url))
web3.eth.defaultAccount = web3.eth.accounts[0]

abi=json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"uint256","name":"_uid","type":"uint256"},{"internalType":"uint256","name":"alloc","type":"uint256"},{"internalType":"uint256","name":"sal","type":"uint256"}],"name":"addBeneficiary","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"authority","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"beneficiaries","outputs":[{"internalType":"uint256","name":"alloc","type":"uint256"},{"internalType":"uint256","name":"sal","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"newAllocation","type":"uint256"}],"name":"changeAllocation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"threshold","type":"uint256"},{"internalType":"uint256","name":"change","type":"uint256"},{"internalType":"int256","name":"greater","type":"int256"}],"name":"changeIndividualAllocation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_uid","type":"uint256"}],"name":"dispense","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getDispensed","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getSurplus","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_uid","type":"uint256"}],"name":"showBeneficiaryAllocation","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]')
address=web3.toChecksumAddress("0x54e92101Da29334A91A5650b63554A5471FCD8a6")

Contract=web3.eth.contract(abi=abi, address=address)

print(Contract.functions.getSurplus().call())

tx_hash = Contract.functions.addBeneficiary(1, 10, 10000).transact()

print(tx_hash)

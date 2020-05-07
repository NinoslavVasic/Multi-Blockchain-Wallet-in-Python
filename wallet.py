
# Importing libraries
import os
import subprocess 
import json

from dotenv import load_dotenv

from constants import *
from bit import Key, PrivateKey, PrivateKeyTestnet
from bit.network import NetworkAPI
from bit import *
from web3 import Web3
from eth_account import Account 


# Web3 connection and loading mnemonic
# Nodes runing with POW
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1.8545"))

# Loading EV
load_dotenv

# Loading Mnemonic EV and (set this mnemonic as an environment variable, and include the one you generated as a fallback using)
mnemonic = os.getenv('MNEMONIC', "twenty type guide fire unknown cube kidney holiday save uniform problem whip erase wink dwarf")
print(mnemonic)

# Functions to transact
#1 create function to call the php file. As I am on windows I am not using standard ./derive but 
def derive_wallets(mnemonic, coin, numderive):
    """Use the subprocess library to call the php file script from Python"""
    command = f'php ./hd-wallet-derive/hd-wallet-derive.php -g --mnemonic="{mnemonic}" --numderive="{numderive}" --coin="{coin}" --format=json' 
    
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
   
    keys = json.loads(output)
    return  keys
 

# Create a coin object to hold child wallets
coins = {"eth", "btc-test", "btc"}
numderive = 3
# Setting the dictionarry
keys = {}
for coin in coins:
    keys[coin]= derive_wallets(os.getenv('mnemonic'), coin, numderive=3)

# Creating a private keys object
eth_PrivateKey = keys["eth"][0]['privkey']
btc_PrivateKey = keys['btc-test'][0]['privkey']


print(json.dumps(eth_PrivateKey, indent=4, sort_keys=True))
print(json.dumps(btc_PrivateKey, indent=4, sort_keys=True))
print(json.dumps(keys, indent=4, sort_keys=True))

#2 - convert private key string 
def priv_key_to_account(coin, priv_key):
    """Convert the privkey string in a child key to an account object that bit or web3.py can use to transact"""
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    if coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)
    
eth_acc = priv_key_to_account(ETH,eth_PrivateKey)
btc_acc = priv_key_to_account(BTCTEST,btc_PrivateKey)

#3 create transaction with necesseary metadata

def create_trx(coin, account, recipient, amount):
    """create the raw, unsigned transaction that contains all metadata needed to transact"""
    global trx_data
    if coin ==ETH:
        gasEstimate = w3.eth.estimateGas(
            {"from": account.address, "to": recipient, "value": amount}
        )
        trx_data = {
            "to": recipient,
            "from": account.address,
            "value": amount,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(account.address)
        }
        return trx_data

    if coin == BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(recipient, amount, BTC)]) 

#4 create, sign, send the transaction 

def send_trx(coin, account, recipient, amount):
    """call create_trx, sign the transaction, then send it to the designated network"""
    if coin == "eth": 
        trx_eth = create_trx(coin,account, recipient, amount)
        sign = account.signTransaction(trx_eth)
        result = w3.eth.sendRawTransaction(sign.rawTransaction)
        print(result.hex())
        return result.hex()
    else:
        trx_btctest= create_trx(coin,account,recipient,amount)
        sign_trx_btctest = account.sign_transaction(trx_btctest)
        from bit.network import NetworkAPI
        NetworkAPI.broadcast_tx_testnet(sign_trx_btctest)       
        return sign_trx_btctest
       






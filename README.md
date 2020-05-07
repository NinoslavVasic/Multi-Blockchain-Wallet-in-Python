<h1>Blockchain with Python </h1>

![](https://github.com/NinoslavVasic/Multi-Blockchain-Wallet-in-Python/blob/master/screenshots/newtons-coin-cradle.jpg)

<h1> MultiWallet<h1>



<h2>Instruction: step by step</h2>

## New startup market race - initial requirement 

<p> Main focus of a newly founded company is to build a portfolio management system (PMS) that supports both, traditional assets
(like gold, silver, stocks, etc) and currently very hot topic - crypto-assets!!! But, as there are so many coins out there, our task to understand how HD wallets work, and to build out a system that can create them.

## Race to the market: Let the games begin !!!

Unfortunately, there aren't as many tools available in Python for this sort of thing, yet.

Thankfully, there is a command line tool, `hd-wallet-derive` that supports not only BIP32, BIP39, and BIP44, but
also supports non-standard derivation paths for the most popular wallets out there today! 

Indeed, we have to develop and integrate the script `wallet.py` at backend with our dearest old friend, Python.

Once we integrate this "universal" wallet, we can use it to manage billions of addresses across 300+ coins, and it will give
us serious edge against the competition.

In this assignment, we will only need to get 2 coins working: Ethereum and Bitcoin Testnet.
Ethereum keys are the same format on any network, so the Ethereum keys should work with your custom networks or testnets. </p>


<p> Dependencies <p>
   
- PHP must be installed on your operating system (any version, 5 or 7). Don't worry, you will *not* need to know any PHP
  (just in case if `./derive` is not working in comand line, which in my experience happened on Windows machine, we will use it as a    backup in one coding line).

- We have to clone the [`hd-wallet-derive`](https://github.com/dan-da/hd-wallet-derive) tool.

- [`bit`](https://ofek.github.io/bit/) Python Bitcoin library.

- [`web3.py`](https://github.com/ethereum/web3.py) Python Ethereum library.



<p> Set-up Project <p>
  
- Create a project directory called `wallet` and `cd` into it.

- Clone the `hd-wallet-derive` tool into this folder and install it using the instructions on its `README.md`.

- Create a symlink called `derive` for the `hd-wallet-derive/hd-wallet-derive.php` script into the top level project
  directory like so: `ln -s hd-wallet-derive/hd-wallet-derive.php derive`
 
  This will clean up the command needed to run the script in our code, as we can call `./derive`
  instead of `./hd-wallet-derive/hd-wallet-derive.php`.

- Test that you can run the `./derive` script properly, use one of the examples on the repo's `README.md`.

#### NOTE: If one get an error running `./derive`, as it can happen on windows machine then use: `php ./hd-wallet-derive/hd-wallet-derive.php`.

- Create a file called `wallet.py` -- this will be your universal wallet script.

Your directory tree should look something like this:

![](https://github.com/NinoslavVasic/Multi-Blockchain-Wallet-in-Python/blob/master/screenshots/tree.png)

### Setup constants file to manage coins

- In a separate file, `constants.py`, set the following constants:
  - `BTC = 'btc'`
  - `ETH = 'eth'`
  - `BTCTEST = 'btc-test'`

- In `wallet.py`, import all constants: `from constants import *`

- Use these anytime you reference these strings, both in function calls, and in setting object keys.

### Generate a Mnemonic phrase

- Generate a new 12 word mnemonic using `hd-wallet-derive` or by using [this tool](https://iancoleman.io/bip39/).

- Set this mnemonic as an environment variable, and include the one you generated as a fallback using:
  `mnemonic = os.getenv('MNEMONIC', 'insert mnemonic here')`

### Deriving a wallet

- Pass as variables Mnemonic (--mnemonic), Coin (--coin) and Numderive (--numderive), then set the --format=json flag,  parse the output   into a JSON object using json.loads(output).And finally pass all into one function, called 'derive_wallets'.
- When done properly, the final object should look something like this (there are only 3 children each in this image):

![](https://github.com/NinoslavVasic/Multi-Blockchain-Wallet-in-Python/blob/master/screenshots/wallet_object.PNG)


## Executing test transactions by calling the functions from `wallet.py` 

   


### BTCTest transaction 

   <p> ```btc_acc = priv_key_to_account(BTCTEST,btc_PrivateKey) ```
       ```create_trx(BTCTEST,btc_acc,"miZgMxdGzSxCTpWazfD2KqhewoUvcQ6CC1", 0.1)``` 
       ```send_trx(BTCTEST,btc_acc,'miZgMxdGzSxCTpWazfD2KqhewoUvcQ6CC1',0.1)```</p>
  
 <p> Confirmation of Executed Transaction </p>

![](https://github.com/NinoslavVasic/Multi-Blockchain-Wallet-in-Python/blob/master/screenshots/btc-confirmation%20-trx.PNG)

### ETH transaction - using local private blockchain

    ```eth_acc = priv_key_to_account(ETH,eth_PrivateKey) ```
    ```create_trx(ETH,eth_acc,"0xba51af165c60A32B3d23Df9B332b4A86cED4A1B9", 1000)``` 
    ```send_trx(ETH, eth_acc,"0xba51af165c60A32B3d23Df9B332b4A86cED4A1B9", 1000)```
     
### Confirmation of Executed Transaction 

![](https://github.com/NinoslavVasic/Multi-Blockchain-Wallet-in-Python/blob/master/screenshots/eth_-trx-conf.PNG)

   


## More details on the:
   - iPNB 'https://github.com/NinoslavVasic/Multi-Blockchain-Wallet-in-Python/blob/master/Multi-Blockchain-Wallet.ipynb'
   - codes:  'https://github.com/NinoslavVasic/Multi-Blockchain-Wallet-in-Python/blob/master/wallet.py'




<footer>
    
Copyright 2020 Columbia Engineering - FinTech Bootcamp NVasic
    
    
</footer>





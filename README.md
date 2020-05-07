<h1>Blockchain with Python </h1>

<h1> MultiWallet<h1>



<h2>Instruction: step by step</h2>

![](https://github.com/NinoslavVasic/Multi-Blockchain-Wallet-in-Python/blob/master/screenshots/newtons-coin-cradle.jpg)



<p>Initial request</p>

<p> Your new startup is focusing on building a portfolio management system that supports not only traditional assets
like gold, silver, stocks, etc, but crypto-assets as well! The problem is, there are so many coins out there! It's
a good thing you understand how HD wallets work, since you'll need to build out a system that can create them.

You're in a race to get to the market. There aren't as many tools available in Python for this sort of thing, yet.
Thankfully, you've found a command line tool, `hd-wallet-derive` that supports not only BIP32, BIP39, and BIP44, but
also supports non-standard derivation paths for the most popular wallets out there today! However, you need to integrate
the script into your backend with your dear old friend, Python.

Once you've integrated this "universal" wallet, you can begin to manage billions of addresses across 300+ coins, giving
you a serious edge against the competition.

In this assignment, however, you will only need to get 2 coins working: Ethereum and Bitcoin Testnet.
Ethereum keys are the same format on any network, so the Ethereum keys should work with your custom networks or testnets. </p>


<p> Dependencies <p>
   
- PHP must be installed on your operating system (any version, 5 or 7). Don't worry, you will *not* need to know any PHP.

- You will need to clone the [`hd-wallet-derive`](https://github.com/dan-da/hd-wallet-derive) tool.

- [`bit`](https://ofek.github.io/bit/) Python Bitcoin library.

- [`web3.py`](https://github.com/ethereum/web3.py) Python Ethereum library.



<p> Set-up Project <p>
  
- Create a project directory called `wallet` and `cd` into it.

- Clone the `hd-wallet-derive` tool into this folder and install it using the instructions on its `README.md`.

- Create a symlink called `derive` for the `hd-wallet-derive/hd-wallet-derive.php` script into the top level project
  directory like so: `ln -s hd-wallet-derive/hd-wallet-derive.php derive`

  This will clean up the command needed to run the script in our code, as we can call `./derive`
  instead of `./hd-wallet-derive/hd-wallet-derive.php`.

- Test that you can run the `./derive` script properly, use one of the examples on the repo's `README.md`
NOTE: If one get an error running ./derive, as it can happen on windows machine then use: 'php ./hd-wallet-derive/hd-wallet-derive.php'

- Create a file called `wallet.py` -- this will be your universal wallet script.

Your directory tree should look something like this:

![](https://github.com/NinoslavVasic/Multi-Blockchain-Wallet-in-Python/blob/master/screenshots/tree.png)

### Setup constants

- In a separate file, `constants.py`, set the following constants:
  - `BTC = 'btc'`
  - `ETH = 'eth'`
  - `BTCTEST = 'btc-test'`

- In `wallet.py`, import all constants: `from constants import *`

- Use these anytime you reference these strings, both in function calls, and in setting object keys.

### Generate a Mnemonic

- Generate a new 12 word mnemonic using `hd-wallet-derive` or by using [this tool](https://iancoleman.io/bip39/).

- Set this mnemonic as an environment variable, and include the one you generated as a fallback using:
  `mnemonic = os.getenv('MNEMONIC', 'insert mnemonic here')`






1. <p> Executing test transactions by calling the functions from `wallet.py` </p>

   


2. <p> BTCTest transaction </p>

   <p> ```btc_acc = priv_key_to_account(BTCTEST,btc_PrivateKey) ```
       ```create_trx(BTCTEST,btc_acc,"miZgMxdGzSxCTpWazfD2KqhewoUvcQ6CC1", 0.1)``` 
       ```send_trx(BTCTEST,btc_acc,'miZgMxdGzSxCTpWazfD2KqhewoUvcQ6CC1',0.1)```</p>
  
 <p> Confirmation of Executed Transaction </p>

![](https://github.com/NinoslavVasic/Multi-Blockchain-Wallet-in-Python/blob/master/screenshots/btc-confirmation%20-trx.PNG)

3. <p> ETH transaction - using local private blockchain, and adding nodes on MyCripto </p>

    <p> ```eth_acc = priv_key_to_account(ETH,eth_PrivateKey) ```
       ```create_trx(ETH,eth_acc,"0xba51af165c60A32B3d23Df9B332b4A86cED4A1B9", 1000)``` 
       ```send_trx(ETH, eth_acc,"0xba51af165c60A32B3d23Df9B332b4A86cED4A1B9", 1000)```</p>
     
<p> Confirmation of Executed Transaction </p>

![](https://github.com/NinoslavVasic/Multi-Blockchain-Wallet-in-Python/blob/master/screenshots/eth_-trx-conf.PNG)

   


<p> More details on the process and codes  </p>
![](https://github.com/NinoslavVasic/Multi-Blockchain-Wallet-in-Python/blob/master/Multi-Blockchain-Wallet.ipynb)



<footer>
    
Copyright 2020 Columbia Engineering - FinTech Bootcamp NVasic
    
    
</footer>





## [Making transactions](https://web3py.readthedocs.io/en/v5/examples.html#id6)[](https://web3py.readthedocs.io/en/v5/examples.html#making-transactions "Permalink to this headline")

There are a few options for making transactions:

-   [`send_transaction()`](https://web3py.readthedocs.io/en/v5/web3.eth.html#web3.eth.Eth.send_transaction "web3.eth.Eth.send_transaction")
    
    Use this method if:
    
    -   you want to send ether from one account to another.
    
-   [`send_raw_transaction()`](https://web3py.readthedocs.io/en/v5/web3.eth.html#web3.eth.Eth.send_raw_transaction "web3.eth.Eth.send_raw_transaction")
    
    Use this method if:
    
    -   you want to sign the transaction elsewhere, e.g., a hardware wallet.
    -   you want to broadcast a transaction through another provider, e.g., Infura.
    -   you have some other advanced use case that requires more flexibility.
    
-   [Contract Functions](https://web3py.readthedocs.io/en/v5/contracts.html#contract-functions)
    
    Use these methods if:
    
    -   you want to interact with a contract. Web3.py parses the contract ABI and makes those functions available via the `functions` property.
    
-   [`construct_sign_and_send_raw_middleware()`](https://web3py.readthedocs.io/en/v5/middleware.html#web3.middleware.construct_sign_and_send_raw_middleware "web3.middleware.construct_sign_and_send_raw_middleware")
    
    Use this middleware if:
    
    -   you want to automate signing when using `w3.eth.send_transaction` or `ContractFunctions`.


___
Type: #microtopic 
Topics: [[Blockchain]], [[Ethereum]], [[1 Fields/Blockchain/Ethereum/Web3.py/Web3.py]]


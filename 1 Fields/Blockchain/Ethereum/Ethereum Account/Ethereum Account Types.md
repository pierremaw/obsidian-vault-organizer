# Externally Owned Accounts (EOA)
- Controlled by a private key.
- Creating an account costs nothing
- Can initiate transactions
- Transactions between externally-owned accounts can only be ETH/token transfers
- Made using a cryptographic pair of keys: public and private keys that control account activities.
# Smart Contract Accounts
- Controlled by code.
- Creating a contract has a cost because you're using network storage
- Can only send transactions in response to receiving a transaction
- Transactions from an external account to a contract account can trigger code which can execute many different actions, such as transferring tokens or even creating a new contract
- Contract accounts don't have private keys. Instead, they are controlled using smart contract logic.
# Similarities
Both account types:
- Can receive, hold and send ETH and tokens
- Can interact with deployed smart contracts
- Have a unique address, represented using a 40-character string that has letters and numbers. An address is a unique identifier for each account on the Ethereum network.

___
Type: #microtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Ethereum Account]]


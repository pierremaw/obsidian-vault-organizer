Internal transactions are transactions that occur between smart contracts. This can also include transactions from a smart contract to an external address when sending ETH to a user. These transactions are labeled internal because every deployed smart contract on the Ethereum blockchain has an assigned internal address.

On the other hand, token transfers are another transaction that occurs between user-created external addresses. An example of this type of transaction is token transfers, such as one user sending an ERC-20 token to another user.

Internal transactions are triggered when an external address calls a smart contract to execute an operation. The contract then will use its built-in logic to start interacting with the other required contracts it needs to complete the operation. Even in a single transaction, a smart contract may need to perform several internal calls to other contracts.

---

## Internal Transaction Example[](https://docs.alchemy.com/docs/what-are-internal-transactions#internal-transaction-example)

A typical example of this transaction flow would be the use of a token exchange.

1. **Token Transfer** - A user starts an exchange of an ERC-20 token by sending their tokens to the exchange's smart contract.
2. **Token Transfer** - The exchange's smart contracts will then deposit the tokens to the smart contract connected to the liquidity pool.
3. **Internal Transaction** - The exchange's contract receives the exchanged amount in WETH (wrapped Ethereum) and then sends that amount to the WETH smart contract to be converted to ETH.
4. **Internal Transaction** - The exchange's contract sends this ETH to the user's external address to complete the exchange.

## Use-Cases[](https://docs.alchemy.com/docs/what-are-internal-transactions#use-cases)

Internal transactions can provide some vital information for your users. Here are a few use-cases where internal transaction information can be used inside a dApp:

1. **Failed Transactions Notifications** -The entire transaction will fail if an internal transaction fails. Informing users exactly where the point of failure helps fix the issue.
2. **Smart Contract Monitoring** - Your deployed smart contract can interact with other contracts via internal transactions. To know when and which contracts it interacts with, you can monitor your smart contract address for any internal transactions.
3. **Blockchain Analytics** - Since internal transactions can be complex, getting insights is helpful. By looking at the number of internal transactions performed by a smart contract, you can understand the popularity and performance of that contract.
4. **Batch Transactions** - If you send a batch of transactions to different sender addresses, you can use internal transactions to more conveniently and securely ensure they reach the right addresses.
___
Type: #subtopic 
Topics: [[Web 3.0]], [[Blockchain]], [[Smart Contracts]]


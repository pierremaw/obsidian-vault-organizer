A transaction is an instruction from an EOA. A transaction is digitially signed, modifes blockchain state and costs gas.

# External Transactions

- **EOA to EOA**: a transaction from one account to another
- **Contract deployment**: a transaction that doesn't have a 'to' address, where the data field is used for the contract code.
  ![[Transactions on Blockchain Networks.png|200]]
- **Smart contract execution**: a transaction that uses a smart contract function.




# Internal transactions

Internal transactions are transactions that occur between smart contracts. This can also include transactions from a smart contract to an external address when sending ETH to a user. These transactions are labeled internal because every deployed smart contract on the Ethereum blockchain has an assigned internal address.

Internal transactions are also referred to as `calls`.

Technically, what happens is that an EOA starts a transaction, and there are interal calls between smart contracts nested within it.

___
Type: #topic
Topics: [[Blockchain]], [[DApps]]


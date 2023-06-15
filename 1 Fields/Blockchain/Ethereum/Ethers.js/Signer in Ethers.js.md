A **Signer** represents an EOA.

| Feature | Description                                                                                                                                                                                                     |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Abstraction                 | A Signer is an abstraction of an Externally Owned Account that can be used to sign messages and transactions and send signed transactions to the Ethereum Network to execute state-changing operations.                 |
| Available Operations        | The available operations of a Signer depend largely on the sub-class used. For example, a Signer from MetaMask can send transactions and sign messages but cannot sign a transaction (without broadcasting it). |
| Wallet                      | A Wallet is a class that knows its private key and can execute any operations with it.                                                                                                                          |
| JsonRpcSigner               | A JsonRpcSigner is connected to a JsonRpcProvider (or sub-class) and is acquired using getSigner.                                                                                                               |




___
Type: #microtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Ethers.js]]


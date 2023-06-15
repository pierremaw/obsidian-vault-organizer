| Topic                    | Information                                                                                                                                                                                                                      |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Contract functions       | Functions defined in a contract can be called from a JavaScript application using Ethers.js.                                                                                                                                     |
| Contract instance        | A contract instance is an instance of a deployed contract that has an address on the blockchain. It can be used to call functions and read data from the contract.                                                               |
| Contract ABI             | The Application Binary Interface (ABI) is a JSON object that describes the interface of a contract, including its functions and their input and output parameters. It is used to encode and decode function calls and responses. |
| Signer                   | A signer is an object that can sign transactions and messages using a private key. In Ethers.js, a signer can be a local account or a hardware wallet.                                                                           |
| Provider                 | A provider is an object that can communicate with the Ethereum network to retrieve data and send transactions. Ethers.js supports several types of providers, including HTTP, WebSocket, and Infura.                             |
| Transaction object       | A transaction object contains the necessary data to send a transaction to the blockchain, including the contract address, function name, input parameters, and gas limit.                                                        |
| Gas limit                | The gas limit is the maximum amount of gas that can be consumed by a transaction. It is set by the user and determines the fee paid for executing the transaction.                                                               |
| Sending a transaction    | To send a transaction that calls a contract function, the user must create a transaction object, sign it with a signer, and send it to the network using a provider.                                                             |
| Waiting for confirmation | After sending a transaction, the user must wait for it to be confirmed by the network. This can be done using the transaction hash and the provider's waitForTransaction function.                                               |
| Handling errors          | If a transaction fails, an error will be thrown. In Ethers.js, errors can be caught and handled using try-catch blocks.                                                                                                          |

___
Type: #microtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Ethers.js]]


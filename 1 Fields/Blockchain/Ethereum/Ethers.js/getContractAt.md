`getContractAt()` is a function found in the `hardhat-ethers` plugin. 

## getContractAt() has 2 variations

1. Get contract using name and address
```
getContractAt(name: string, address: string, signer?: ethers.Signer)
```

2. Get contract using abi and address
```
getContractAt(abi: any[], address: string, signer?: ethers.Signer)
```

| Feature | Description                                                                                                                                                              |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| getContractAt               | A function in the Hardhat-Ethers library that creates an instance of an existing contract using either 1) It's name and address. 2) It's ABI and address.                                                         |
| Address                     | The address of the deployed contract on the Ethereum network. It is a unique identifier that is used to interact with the contract on the blockchain.                    |
| ABI                         | Stands for Application Binary Interface, it describes how to interact with the contract's functions, variables, and events.                                              |
| Contract Instance           | An instance of a deployed contract that can be interacted with.                                                                                                          |
| Promise-based               | The getContractAt function returns a promise that resolves to a contract instance. This allows for asynchronous execution and better handling of errors.                 |
| Contract Methods            | The functions that are defined in the contract and can be called through the contract instance. These methods interact with the state of the contract on the blockchain. |


___
Type: #microtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Ethers.js]]


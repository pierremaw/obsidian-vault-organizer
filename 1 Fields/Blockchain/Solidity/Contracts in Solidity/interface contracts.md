**A Solidity contract interface is a list of function definitions without implementation.** In other words, an interface is a description of all functions that an object must have for it to operate. The interface enforces a defined set of properties and functions on a contract.

| Features | Description                                                                                                                           |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Definition                     | List of function definitions without implementation                                                                                   |
| Enforcement                    | Enforces a defined set of properties and functions on a contract                                                                      |
| Interoperability               | Allows interaction with other contracts without having their code by using their interface                                            |
| Code Duplication               | Reduces code duplication and overhead                                                                                                 |
| Extensibility                  | Useful for decentralized applications that require extensibility and want to avoid complexity                                         |
| Inheritance                    | Can inherit from other interfaces and be inherited by contracts                                                                       |
| Override                       | Functions that inherit from the interface must set the override modifier on every function that overrides an interface function       |
| Abstract Contracts             | Abstract contracts possess at least one function that lacks implementation                                                            |
| Base Contracts                 | Abstract contracts can be used as base contracts from which other contracts can inherit                                               |
| ABI Representation             | Interfaces are limited to what the contract’s Application Binary Interface (ABI) can represent                                        |
| Information Loss               | Conversion between the ABI and an interface is possible without any information loss                                                  |
| Declaration                    | Declared with the “interface” keyword                                                                                                 |
| Implementation                 | Can be used to communicate with another contract or to implement the interface                                                        |
| Inheritance                    | Can be inherited by contracts using the “is” keyword                                                                                  |
| Restrictions                   | Cannot have any functions implemented, can only have external functions, cannot declare a constructor, cannot declare state variables |


___
Type: #microtopic 
Topics: [[Blockchain]], [[Solidity]], [[Contracts in Solidity]]


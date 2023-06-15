**Interfaces** are used to make function calls between contracts.

| Feature        | Description                                                                                                                         |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Solidity Interface                 | A list of function definitions without implementation                                                                               |
| Interacting with other contracts   | Using their interface, you can interact with other contracts and call their functions                                               |
| Interface keyword                  | Used to identify interfaces in Solidity                                                                                             |
| Inheritance                        | Solidity interfaces can inherit from other interfaces and be inherited by contracts                                                 |
| Override modifier                  | All functions that inherit from the interface must set the override modifier on every function that overrides an interface function |
| Data types                         | Defined inside interfaces and can be accessed from other contracts                                                                  |
| Abstract contracts                 | Have at least one function lacking implementation and cannot be compiled, but can be used as base contracts for inheritance         |
| Application Binary Interface (ABI) | Limits what an interface can represent                                                                                              |
| Creating an interface              | Declared at the top of your program with the “interface” keyword                                                                    |
| Implementation                     | An interface can be implemented by inheriting and implementing its functions in a contract                                          |
| Interface restrictions             | Cannot have functions implemented, declare a constructor or state variables. Functions must be of type external                     |


# ISwapRouter Interface for Uniswap

In the case of the ISwapRouter for Uniswap, the interface is defined in a separate file because it allows for better organization and modularity of the code.

Defining the interface in a separate file also allows other contracts to import and use it without having to include unnecessary code from the contract implementation file. Additionally, having the interface in a separate file makes it easier to update and maintain the interface as changes to the contract implementation are made.

In general, separating the interface from the implementation can help make code more modular, easier to maintain, and easier to test.

___
Type: #microtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Solidity]], [[Solidity Smart Contract]]


Abstract contracts cannot be instantiated and serve as a blueprint for other contracts.

| Feature | Description                                                                                                                                                                                                           |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Abstract contracts          | Solidity contracts that cannot be instantiated and serve as a blueprint for other contracts                                                                                                                           |
| Implementation              | Abstract contracts are marked as abstract when at least one of their functions is not implemented or when they do not provide arguments for all of their base contract constructors                                   |
| Comparison to interfaces    | Abstract contracts are similar to interfaces but are less limited in what they can declare                                                                                                                            |
| Syntax                      | Abstract contracts are declared using the abstract keyword                                                                                                                                                            |
| Instantiation               | Abstract contracts cannot be instantiated directly, even if they implement all defined functions                                                                                                                      |
| Inheritance                 | A contract that inherits from an abstract contract and does not implement all non-implemented functions by overriding must also be marked as abstract                                                                 |
| Advantages                  | Abstract contracts decouple the definition of a contract from its implementation, provide better extensibility and self-documentation, and facilitate patterns like the Template method and removing code duplication |
| Use cases                   | Abstract contracts are useful for defining methods that any child of the contract must implement, similar to defining methods in an interface                                                                         |
| Limitations                 | Abstract contracts cannot override an implemented virtual function with an unimplemented one                                                                                                                          |

___
Type: #microtopic 
Topics: [[Blockchain]], [[Solidity]], [[Contracts in Solidity]]


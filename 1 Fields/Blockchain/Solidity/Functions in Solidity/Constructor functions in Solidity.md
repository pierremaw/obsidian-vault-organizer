A **constructor** is an optional function declared with the constructor keyword, which is executed upon contract creation, and where contract initialization can be run

| Feature | Description                                                                                                                                                                                                                                                                                                                  |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Constructor                 | An optional function declared with the constructor keyword, which is executed upon contract creation, and where contract initialization code can be run.                                                                                                                                                                     |
| State Variables             | Variables declared in the contract storage that hold the state of the contract. They can be initialized inline, or they will have a default value if not initialized.                                                                                                                                                        |
| Deployment Cost             | The cost of deploying the code to the blockchain after the constructor has run. It is linear to the length of the code and includes all public interface functions and functions that are reachable through function calls. It does not include the constructor code or internal functions only called from the constructor. |
| Default Constructor         | The default constructor is equivalent to constructor() {}. If there is no constructor declared in the contract, the default constructor is assumed.                                                                                                                                                                          |
| Internal Parameters         | Parameters that can be used in a constructor, such as storage pointers. The contract must be marked abstract if internal parameters are used because they cannot be assigned valid values from outside but only through the constructors of derived contracts.                                                               |



___
Type: #microtopic 
Topics: [[Blockchain]], [[Solidity]], [[Functions in Solidity]]


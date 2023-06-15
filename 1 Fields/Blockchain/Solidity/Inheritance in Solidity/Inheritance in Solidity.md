| Feature                             | Description                                                                                                                                                                                                                                                       |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Multiple Inheritance                | Solidity supports multiple inheritance, which means a derived contract can inherit from more than one base contract.                                                                                                                                              |
| Polymorphism                        | Solidity allows for polymorphism, meaning a function call always executes the function of the same name and parameter types in the most derived contract in the inheritance hierarchy.                                                                            |
| Function Overriding                 | In order to enable polymorphism, each function in the inheritance hierarchy must be explicitly enabled using the virtual and override keywords.                                                                                                                   |
| Calling Functions in Base Contracts | A function in a derived contract can call a function in a base contract by explicitly specifying the contract using ContractName.functionName() or by using super.functionName() to call the function one level higher up in the flattened inheritance hierarchy. |
| State Variable Shadowing            | A derived contract can only declare a state variable with a name that is not already used in any of its base contracts. Shadowing is considered an error.                                                                                                         |
| Inherited Code Compilation          | When a contract inherits from other contracts, only a single contract is created on the blockchain, and the code from all the base contracts is compiled into the created contract.                                                                               |

	         Base class
	/                 \
Derived class 1       Derived class 2


___
Type: #subtopic 
Topics: [[Blockchain]], [[Solidity]]


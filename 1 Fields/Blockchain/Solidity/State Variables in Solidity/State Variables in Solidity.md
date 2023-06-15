**State Variables** are stored in the contract's persistent memory. Modifying a state variable in one transaction will change its value for anyone who tries to read the variable afterwards.

In Solidity, declaring a state variable is as simple as declaring the variable inside the contract:

```solidity
contract Contract {
	bool myVariable;
}
```

| Visibility Modifier | Description                                                                                                                              | Access Level |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| Public              | State variables with the public modifier can be accessed by any contract                                              | Read/write   |
| Internal            | State variables with the internal modifier can only be accessed within the contract in which they were defined and by a derived contract | Read/write   |
| Private             | State variables with the private modifier can only be accessed by the main contract in which they were declared                          | Read/write   |
| Default             | When the visibility modifier is not defined, the default value is internal                                                               | Read/write   |

___
Type: #subtopic  
Topics: [[Blockchain]], [[Ethereum]], [[Solidity]], [[Variables in Solidity]]

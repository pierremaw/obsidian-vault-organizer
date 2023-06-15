`pure`, `view`, and `payable` are mutability modifiers in solidity.

# `pure`

A `pure` function does not read or modify the state of the contract. 

```
function square(uint256 x) public pure returns (uint256) {
	return x * x; 
}
```

# `view`

A `view` function is able to read data from the contract but does not modify it.

```
function getBalance(address account) public view returns (uint256) {
    return balances[account];
}

```

# `payable`

A `payable` function is able to receive ether.
```
function deposit() public payable {
	balances[msg.sender] += msg.value; 
}
```

# default mutability modifier

If a function has no mutability modifier specified, it defaults to `non-payable`.

A `non-payable` function cannot receiver ether but it can view and update the contract's state.

___
Type: #microtopic 
Topics: [[Blockchain]], [[Solidity]], [[Ethereum]], [[Functions in Solidity]], [[Function Modifiers in Solidity]]


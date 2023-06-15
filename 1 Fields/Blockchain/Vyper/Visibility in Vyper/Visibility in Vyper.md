When you create a function, variable, or struct in a Vyper contract, you can specify its visibility. Visibility determines whether the item can be accessed from within the contract, or whether it is visible to other contracts or outside of the blockchain entirely.

# Visibility Levels

There are three levels of visibility in Vyper:

## @public

The `@public` decorator in Vyper is used to mark a state variable or function as publicly accessible. When a state variable or function is marked as `@public`, it can be accessed from outside the contract by anyone who knows the contract's address.
```vyper
@public 
def myFunction() -> int128:     
	return 123
```


## @external

External functions can only be called from outside the contract, and not from other functions within the contract.
```vyper
@external 
def myFunction() -> int128:
	return 123
```


## @private

Private functions and variables can only be accessed within the contract.
```vyper
myVar: uint256  

@private 
def myFunction():
	self.myVar = 123
```

# When to use which visibility level

Here are some general guidelines on when to use each visibility level:

- Use public functions and variables when you want to make them accessible to other contracts.
- Use external functions when you want to make them callable from outside the contract, but not from other functions within the contract.  
- Use private functions and variables when you want to keep them hidden from other contracts and outside the blockchain.

___
Type: #subtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]]


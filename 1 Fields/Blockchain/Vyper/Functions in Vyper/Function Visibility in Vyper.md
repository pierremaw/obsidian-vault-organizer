In Vyper, you can specify a function's visibility using the `@public` or `@external` decorator. 

The `@public` decorator makes the function visible to other contracts and can be called internally. 

The `@external` decorator makes the function only callable from outside the contract.

```vyper
@public
def my_public_function(): 
	# function body 

@external 
def my_external_function(): 
	# function body
```

___
Type: #microtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]], [[Functions in Vyper]]


Function modifiers are used to add additional logic to a function. Function modifers are functions themselves.

You can apply a modifier to a function using the `@modifier` decorator. 

Here's an example:

```vyper
@modifier onlyOwner():     
	require(msg.sender == self.owner)
	
@external 
@onlyOwner 
def my_function():     
	# function body
```

In this example, we define a modifier called `onlyOwner` that requires that the caller of the function is the owner of the contract. We then apply the modifier to the `my_function` function using the `@onlyOwner` decorator.
___
Type: #microtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]], [[Functions in Vyper]]


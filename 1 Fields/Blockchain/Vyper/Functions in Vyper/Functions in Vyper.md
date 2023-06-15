Functions are executable units of code within a contract.

# Function Definition

To define a function in Vyper, you use the `def` keyword, then specify the function name. You can also define arguments that the function will take. Here's an example:

```vyper
@external 
def my_function(arg1: uint256, arg2: String[100]) -> bool:     
	# function body
```

In this example, we define a function called `my_function`.

There are two parameters. Parameter 1's name is arg1 and it's type is uint256. Parameter 2's name is arg2 and it's type is String[100]

# Function Visibility

In Vyper, you can specify the visibility of a function using the `@external` or `@external` decorator. 

## @external

External functions (marked with the `@external` decorator) are a part of the contract interface and may only be called via transactions or from other contracts.

```
@external
def add_seven(a: int128) -> int128:
    return a + 7
```

A Vyper contract cannot call directly between two external functions. If you must do this, you can use an [interface](https://docs.vyperlang.org/en/v0.3.7/interfaces.html#interfaces).

## @internal

The `@internal` decorator makes the function only callable from other functions within  the same contract.

```vyper

@external
def my_public_function(): 
	# function body 

@external 
def my_external_function(): 
	# function body
```


# Function Mutability

You can optionally declare a function’s mutability by using a [decorator](https://docs.vyperlang.org/en/v0.3.7/control-structures.html#function-decorators). There are four mutability levels:

**`@pure`** functions do not read any state or global variables.`@pure` functions can only call other `@pure` functions.

**`@view`** functions can read state variables, global variables, and call internal functions. However, `@view` functions cannot call @payable or @nonpayable functions

**`@payable`** functions can receive ether
> Functions default to `nonpayable` when no mutability decorator is used.


Functions marked with `@pure` cannot call non-`pure` functions.

___
Type: #subtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]]


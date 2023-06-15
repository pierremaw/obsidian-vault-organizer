# Function Mutability

You can optionally declare a function’s mutability by using a [decorator](https://docs.vyperlang.org/en/v0.3.7/control-structures.html#function-decorators). There are four mutability levels:

## Pure
Does not read from the contract state or any environment variables.

## View
May read from the contract state, but does not alter it.

## Nonpayable
May read from and write to the contract state, but cannot receive Ether.

## Payable
May read from and write to the contract state, and can receive Ether.

```vyper
@view
@external
def readonly():
    # this function cannot write to state
    ...

@payable
@external
def send_me_money():
    # this function can receive ether
    ...
```

Functions default to `nonpayable` when no mutability decorator is used.

Functions marked with `@view` cannot call mutable (`payable` or `nonpayable`) functions. Any external calls are made using the special `STATICCALL` opcode, which prevents state changes at the EVM level.

Functions marked with `@pure` cannot call non-`pure` functions.


___
Type: #microtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]], [[Functions in Vyper]]


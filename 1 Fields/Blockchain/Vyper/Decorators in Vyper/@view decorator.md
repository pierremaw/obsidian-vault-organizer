@view functions can read state variables, global variables, and call internal functions.

```Vyper
@external
@view
def getTokenPrice() -> uint256:
    return 100
```

In this example, the `getTokenPrice` function is marked as both `@external` and `@view`. This means that the function can be called by anyone and returns the current price of a token, but does not modify the contract state in any way.

A `@view` funcion must also be marked as `@external`.
___
Type: #microtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]], [[Decorators in Vyper]]


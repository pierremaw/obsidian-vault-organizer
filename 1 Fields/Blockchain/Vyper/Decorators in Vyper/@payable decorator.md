The `@payable` decorator is used to mark a function as able to receive Ether as part of a transaction. Here's an example:

 ```Vyper
 @external
@payable
def buyToken() -> bool:
    # process payment and transfer tokens to buyer
    return True
```

In this example, the `buyToken` function is marked as both `@external` and `@payable`. This means that the function can be called by anyone and can receive Ether as part of the transaction. The function processes the payment and transfers tokens to the buyer, and returns `True`.

Note that any function that is marked as `@payable` must also be marked as `@external`.
___
Type: #microtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]], [[Decorators in Vyper]]


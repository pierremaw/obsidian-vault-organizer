A contract can have a `__default__` function, executed when a function that does not exist is called. This is the same function as the fallback function in Solidity.

This function is named `__default__` and it is commonly used to receive Ether.

```
event Payment:
    amount: uint256
    sender: indexed(address)

@external
@payable
def __default__():
    log Payment(msg.value, msg.sender)
```
___
Type: #microtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]], [[Functions in Vyper]]


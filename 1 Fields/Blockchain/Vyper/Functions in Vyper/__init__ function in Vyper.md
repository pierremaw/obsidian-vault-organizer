`__init__` is a special initialization function that may only be called at the time of deploying a contract. It can be used to set initial values for storage variables. A common use case is to set an `owner` variable with the creator the contract:

```vyper
owner: address

def __init__():
    self.owner = msg.sender
```

You cannot call to other contract functions from the initialization function.

___
Type: #microtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]], [[Functions in Vyper]]


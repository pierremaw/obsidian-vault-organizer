Vyper has a handy way to secure your contract from re-entrancy.

A re-entrancy lock can be created on a function with `@nonreentrant("lock")`.

Functions can be locked together by using the same name for the locks.
```
# @version ^0.3.7


@external
@nonreentrant("lock")
def func0():
    # call back msg.sender
    raw_call(msg.sender, b"", value=0)


@external
@nonreentrant("lock-2")
def func1():
    raw_call(msg.sender, b"", value=0)


@external
@nonreentrant("lock-2")
def func2():
    raw_call(msg.sender, b"", value=0)

```
___
Type: #microtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]], [[Functions in Vyper]]


Checks that a specified condition is true.

If the condition specified in the `assert` statement evaluates to `false`, the contract reverts and any changes made are discarded.

The `assert` statement takes a single input parameter, which should evaluate to a boolean value.

```vyper
# format
assert (condition), message

# example
assert x == 10, "x is not equal to 10"
```

`assert`'s behavior is equivalent to:
```
if not (condition):
    print(message)
```

___
Type: #microtopic  
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]], [[Statements in Vyper]]


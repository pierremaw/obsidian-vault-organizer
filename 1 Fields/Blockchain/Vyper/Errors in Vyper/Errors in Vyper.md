# `assert` & `raise`

Use `assert` and `raise` to check inputs and validate state.

When an error occurs, it will halt the entire function call, undoing any changes.

You will still need to pay gas for the failed transaction.

## `assert`

Checks if a condition is true.

```vyper
assert (condition), message
```

Equal to:
```
if not (condition):
	print(message)
```

## `raise`


___
Type: #subtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]]


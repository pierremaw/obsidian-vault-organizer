
The `@external` decorator is used to mark a function as externally callable. This means that the function can be called by anyone, even if they are not part of the contract. Here's an example:

```Vyper
@external def getName() -> String[50]:     return "Alice"
```

In this example, the `getName` function is marked as `@external`, which means that it can be called by anyone who knows the contract address. The function returns the string "Alice".

___
Type: #microtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]], [[Decorators in Vyper]]


# return

`return` leaves the current function call with the expression list (or None) as a return value.

```
return RETURN_VALUE
```

> An important distinction between Vyper and Python is that Vyper does not implicitly return `None` at the end of a function if no `return` statement is given. All functions must end with a `return` statement, or another terminating action such as `raise`.

It is not allowed to have additional, unreachable statements after a `return` statement.

___
Type: #subtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]], [[Statements in Vyper]]


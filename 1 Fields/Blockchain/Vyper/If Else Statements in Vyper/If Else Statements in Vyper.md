# If/Else Statements

If/else statements allow you to execute different code blocks depending on a condition. Here's how to use them in Vyper:

## Syntax

```vyper
if condition:
    # code to execute if the condition is true
else:
    # code to execute if the condition is false
```

## Example

```vyper
a: uint256
b: uint256

@external
def setValues(_a: uint256, _b: uint256):
    if _a > _b:
        self.a = _a
    else:
        self.b = _b
```


In this example, if the value of `_a` is greater than the value of `_b`, then the value of `self.a` is set to `_a`. Otherwise, the value of `self.b` is set to `_b`.
___
Type: #subtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]]


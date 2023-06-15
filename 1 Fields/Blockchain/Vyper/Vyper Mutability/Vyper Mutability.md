Mutability refers to the ability of a function to modify state variables. In Vyper, functions can have different levels of mutability, which are defined using function decorators.

# Pure

A pure function is one that does not modify state variables and only returns a value.
```vyper
@pure
def multiply(a: int128, b: int128) -> int128:
    return a * b

```

# View

A view function is one that does not modify state variables but may read from them.
```vyper
@view
def get_balance() -> uint256:
    return self.balance

```

# Nonpayable

A nonpayable function is one that can modify state variables but cannot receive ether.
```
@nonpayable
def set_name(name: String[50]):
    self.name = name

```

# Payable

A payable function is one that can modify state variables and can receive ether.
```vyper
@payable
def deposit() -> uint256:
    self.balance += msg.value
    return self.balance

```


___
Type: #subtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]]


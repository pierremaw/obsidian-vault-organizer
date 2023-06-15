
# Integer

### int128
```vyper
i: public(int128)
```

This defines an integer variable named `i`, which can hold a signed integer value between -2^127 and 2^127 - 1. This variable can be used to represent numeric data that does not require decimal places.

### uint256
```vyper
u: public(uint256)
```

This defines an unsigned integer variable named `u`, which can hold an unsigned integer value between 0 and 2^256 - 1. This variable can be used to represent numeric data that does not require decimal places and cannot be negative.

# Decimal

```vyper
d: public(decimal)
```

This defines a decimal variable named `d`, which can hold a fixed-point decimal value with up to 18 decimal places. This variable can be used to represent numeric data that requires decimal places, such as currency amounts.

# String

```vyper
s: public(String[100])
```

This defines a string variable named `s`, which can hold a variable-size array of up to 100 characters. This variable can be used to represent text data of any length.

# Boolean

```vyper
b: public(bool)
```

This defines a boolean variable named `b`, which can have the value `True` or `False`. This variable can be used to represent binary logic, such as whether a condition is true or false.

# Address

```vyper
addr: public(address)
```

This defines an address variable named `addr`, which can hold an Ethereum address. This variable can be used to represent Ethereum accounts or contracts.

# [[Bytes]]

```vyper
bites: public(Bytes[100])
```

This defines a Bytes variable named `bites`, which can hold a variable-size array of up to 100 bytes. This variable can be used to represent binary data of any length.

# [[Bytes32]]

```vyper
b32: public(bytes32)
```

This defines a bytes32 variable named `b32`, which can hold a fixed-size array of 32 bytes. This variable can be used to represent data that is exactly 32 bytes long, such as cryptographic hashes.

___
Type: #subtopic  
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]]


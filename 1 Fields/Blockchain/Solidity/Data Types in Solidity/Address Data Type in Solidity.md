The address data type represents a 20-byte (160-bit) Ethereum address.

# Key features and applications

- An Ethereum address is the unique identifier of an account on the Ethereum blockchain, and it can receive or send Ether or other ERC20 tokens.
- Solidity uses the `address` type to represent Ethereum addresses in smart contracts.
- Ethereum addresses are represented as 20-byte values, so `address` is a fixed-size data type.
- The `address` type has methods for transferring Ether and calling functions on other smart contracts.


# Creating address variables

Solidity supports the declaration of `address` variables, which can be used to store Ethereum addresses.

Addresses can be declared using the `address` keyword, followed by the variable name, as shown below:

```
address public myAddress;
```


# Address operations

The `address` type has several built-in functions and operations, which can be used to manipulate Ethereum addresses.

### `balance` returns the balance of the address in Wei.

```
address payable recipient = payable(0x1234567890123456789012345678901234567890); uint balance = recipient.balance;

```

### `send` can be used to send Ether to an address. It returns `true` if the transfer was successful and `false` otherwise.

```
address payable recipient = payable(0x1234567890123456789012345678901234567890); recipient.send(1 ether);
```

### `transfer` can also be used to send Ether to an address, but it will revert the transaction if the transfer fails.

```
address payable recipient = payable(0x1234567890123456789012345678901234567890); recipient.transfer(1 ether);
```

### `call` and `delegatecall` are used to call external functions on other contracts. The former forwards all remaining gas to the external contract, while the latter does not.

```
address contractAddress = 0x1234567890123456789012345678901234567890; bool success = contractAddress.call(abi.encodeWithSignature("myFunction(uint256)", 123));
```

### `selfdestruct` can be used to destroy the current contract and send all its remaining Ether to another address.

```
address payable recipient = payable(0x1234567890123456789012345678901234567890); selfdestruct(recipient);
```


# Address types

- There are two types of addresses in Solidity: `address` and `address payable`.
- `address` is a read-only type and can only be used for value transfer, while `address payable` can be used for both value transfer and receiving Ether.

```
address public myAddress; 
address payable public myPayableAddress;
```


# Converting between address types

### An `address` can be converted to `address payable` using the `payable` keyword.
```
address public myAddress;
address payable myPayableAddress = payable(myAddress);
```

### It is also possible to convert a `uint160` value to an `address` type using typecasting.
```
uint160 public myUint;
address public myAddress = address(myUint);
```

___
Type: #microtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Solidity]], [[Data Types in Solidity]]


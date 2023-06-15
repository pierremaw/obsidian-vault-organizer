

## Sending Ether

To send ether from one address to another in Vyper, you can use the `send` function. Here's how:

1.  Define the function that will send ether, and include the recipient's address and the amount of ether to send as arguments.
```vyper
@external
def sendEther(recipient: address, amount: uint256):
```

2.  Use the `send` function to transfer the specified amount of ether to the recipient's address.
```vyper
send(recipient, amount)
```

3.  Include a `require` statement to ensure that the contract has enough ether to send.
```vyper
require(self.balance >= amount, "Insufficient balance")
```

Here's an example of a complete function that sends ether:
```vyper
@external
def sendEther(recipient: address, amount: uint256):
    require(self.balance >= amount, "Insufficient balance")
    send(recipient, amount)
```

## Receiving Ether
To receive ether in Vyper, you can use a fallback function. A fallback function is a special function that is executed when ether is sent to a contract without specifying a function to call. Here's how:

1.  Create a fallback function that includes the `payable` modifier, which allows the function to receive ether.
```vyper
@external
@payable
def __default__():
```

2. Add the logic for the function. This can include updating state variables or emitting an event to indicate that ether has been received.
```vyper
self.balance += msg.value
```

Here's an example of a complete fallback function that receives ether:
```vyper
@external
@payable
def __default__():
    self.balance += msg.value
```

Note that the fallback function must include the `payable` modifier in order to receive ether. If a contract does not have a fallback function that is payable, any ether sent to the contract will be rejected.

## Conclusion

Sending and receiving ether is an important part of developing smart contracts on the Ethereum network. By following the steps outlined in this guide, you can ensure that your contracts can send and receive ether safely and reliably.
___
Type: #subtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]]


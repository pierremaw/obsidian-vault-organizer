There are two ways to send Ether from a contract:

1. `send`
2. `raw_call`

# send

The `send` is a built-in function. It is used to transfer ether from one address to another. 

It is typically used to transfer ether between two accounts or to send ether to a contract.

## parameters
```
(To address, To amount)
```

## return values
```
boolean value that indicates whether the transfer was successful.
```

## usage
```
@external
def sendEther(to: address, amount: uint256):
    # when Ether is sent to a contract it will call 
    # __default__ inside the receiving contract
    # forwards 2300 gas
    send(to, amount)    
```


# raw_call

`raw_call` is a low level function. It is used to call and send Ether to other functions.

## parameters
```
(To address, data, gas amount, ether amount, buffer size )
```

## return values
```
A byte string
```

## usage
```

```
___
Type: #microtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]], [[Built-in Functions in Vyper]]


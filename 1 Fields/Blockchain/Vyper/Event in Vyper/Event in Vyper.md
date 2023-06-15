Events write logs to the blockchain, commonly used by application to monitor blockchain state and as a cheaper alternative to store data on the blockchain without using state variables.

Events can be efficiently searched by indexing their arguments. Up to 3 parameters can be indexed.

# Defining Events

To define an event in Vyper, use the `event` keyword, followed by the event name and its parameters.
```vyper
event Log:
	sender: indexed(address)
	message: String[100]
```

# Logging Events
Once you have defined an event in your Vyper contract, you can emit the event using the `log` keyword. Here's an example:

```vyper
log Log(msg.sender, message)
```

In this example, we emit a `Transfer` event with `msg.sender`, `recipient`, and `amount` as its parameters. The `msg.sender` parameter is a built-in Vyper function that returns the address of the account that called the current function.


# Listening for Events

Once an event has been emitted, it can be captured by other contracts or external applications using the Web3 library's `getLogs` method. Here's an example:

```vyper
from web3 import Web3

web3 = Web3(provider)

transfer_filter = contract.events.Transfer.createFilter(fromBlock='earliest', toBlock='latest', argument_filters={'from': my_address})

for transfer_event in transfer_filter.get_all_entries():
    # process the transfer_event

```

In this example, we create a filter for `Transfer` events that have `my_address` as the `from` parameter, and then process each event that matches that filter.

___
Type: #subtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]]


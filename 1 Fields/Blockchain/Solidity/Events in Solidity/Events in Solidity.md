| Concept            | Description                                                                                                                                                                                                     |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Events             | Abstraction on top of the EVM's logging functionality, which allow applications to subscribe and listen to events through the RPC interface of an Ethereum client.                                              |
| Inheritance        | Events are inheritable members of contracts.                                                                                                                                                                    |
| Storage            | When an event is called, its arguments are stored in the transaction's log, which is a special data structure in the blockchain associated with the contract's address.                                         |
| Visibility         | Logs and their event data are not accessible from within contracts, not even from the contract that created them.                                                                                               |
| Merkle proof       | It is possible to request a Merkle proof for logs, so if an external entity supplies a contract with such a proof, it can check that the log actually exists inside the blockchain.                             |
| Indexed attributes | You can add the attribute indexed to up to three parameters, which adds them to a special data structure known as "topics" instead of the data part of the log. A topic can only hold a single word (32 bytes). |
| Encoding           | All parameters without the indexed attribute are ABI-encoded into the data part of the log.                                                                                                                     |
| Searching          | Topics allow you to search for events, for example when filtering a sequence of blocks for certain events. You can also filter events by the address of the contract that emitted the event.                    |

___
Type: #subtopic 
Topics: [[Blockchain]], [[Solidity]]


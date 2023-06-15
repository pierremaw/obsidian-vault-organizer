| Feature | Description                                                                                                                                                                                                                                                                                                                       |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Physical Instantiation      | The EVM exists as one single entity maintained by thousands of connected computers running an Ethereum client.                                                                                                                                                                                                                    |
| Purpose                     | The Ethereum protocol exists solely for the purpose of keeping the continuous, uninterrupted, and immutable operation of the EVM, which is the environment in which all Ethereum accounts and smart contracts live.                                                                                                               |
| Canonical State             | At any given block in the chain, Ethereum has one and only one 'canonical' state, and the EVM defines the rules for computing a new valid state from block to block.                                                                                                                                                              |
| State Transition Function   | The EVM behaves as a mathematical function, given an old valid state (S) and a new set of valid transactions (T), the Ethereum state transition function Y(S, T) produces a new valid output state S'.                                                                                                                            |
| State                       | In the context of Ethereum, the state is an enormous data structure called a modified Merkle Patricia Trie, which keeps all accounts linked by hashes and reducible to a single root hash stored on the blockchain.                                                                                                               |
| Transactions                | Transactions are cryptographically signed instructions from accounts, and there are two types: those which result in message calls and those which result in contract creation.                                                                                                                                                   |
| Contract Creation           | Contract creation results in the creation of a new contract account containing compiled smart contract bytecode.                                                                                                                                                                                                                  |
| EVM Instructions            | The EVM executes as a stack machine with a depth of 1024 items, and compiled smart contract bytecode executes as a number of EVM opcodes that perform standard stack operations like XOR, AND, ADD, SUB, etc. The EVM also implements a number of blockchain-specific stack operations, such as ADDRESS, BALANCE, BLOCKHASH, etc. |


![[EVM.png]]


___
Type: #subtopic 
Topics: [[Blockchain]], [[Ethereum]]


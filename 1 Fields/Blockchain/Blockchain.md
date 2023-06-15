| Topic               | Information                                                                                                                                                                                                                          |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Definition          | A public database that is maintained using many computers in a network.                                                                                                                                                      |
| Block               | A collection of transactions that have been been proposed by a miner and validated by the blockchain network.                                                                   |
| Chain               | Refers to the fact that each block cryptographically references its parent, and blocks get chained together. Data in a block cannot change without changing all subsequent blocks, requiring consensus from the entire network.      |
| Nodes               | Computers in the network that ensure everyone interacting with the blockchain has the same data.                                                                                                                                     |
| Consensus Mechanism | A mechanism that allows every computer in the network to agree upon each new block and the chain as a whole. Bitcoin uses a POW (Proof of Work) consensus mechanism, while Ethereum uses a POS (Proof of Stake) consensus mechanism. |

## Blockchain = Globally Shared Transaction Database

![[Blockchain-1.png]]

Transactions are so important, that one can refer to a blockchain as a globally shared, transactional database. They are the heart and soul of what drives the state changes behind Ethereum.

## P2P Network

Not only are blockchains globally-shared databases, they are globally-shared **decentralized** databases:
![[Blockchain-2.png]]

Every node keeps a copy of the latest Ethereum world state. When a new block packed full of state-changing transactions gets mined, the block is independently verified by every node in the peer-to-peer network. If the block is truthful (no double spending transactions, all digital signatures check out, etc) then the node adds that block to their own local version of the blockchain as the latest representation of the Ethereum world state. This happens every time a block is mined: worldState`n` transitions to worldState`n+1` and so on.
![[Blockchain-3.png]]
The Ethereum network is made up of nodes decentralized all over the world. Each of these nodes performs verification on any new block of transactions being added to the Ethereum blockchain.

We've learned that in order to interact with one of these nodes constituting the Ethereum P2P network, one must send a JSON-RPC request (in order to read data, which anyone can do!) or send a _signed_ JSON-RPC request (in order to write data, which means you are changing some state in the Ethereum computer).

> Remember, a "_signed_ JSON-RPC request" is just fancy a fancy term for transaction.

![[Blockchain-4.png]]
As the diagram above shows, as an EOA, you have three routes to interact with the Ethereum computer via a connection to an Ethereum node:

1.  **Contract creation**: As an EOA, you deploy a new smart contract to the Ethereum computer _via a special transaction_ (signed JSON-RPC request)
2.  **Message call**: As an EOA, you either send some ETH to another EOA or interact with a smart contract in some way _via a transaction_ (signed JSON-RPC request)
3.  **Inspection**: Any user can make read queries to any Ethereum nodes, no account needed. Try out the `eth_getBalance` method in the [Alchemy Composer](https://composer.alchemy.com/) if you don't believe us! (non-signed JSON-RPC request)

___
Type: #field 
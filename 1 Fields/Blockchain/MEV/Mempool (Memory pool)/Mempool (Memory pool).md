A data structure that stores unconfirmed transactions that are waiting to be included in a block. The mempool is generally a priority queue where transactions with higher gas prices are given priority over those with lower gas prices.

## What is a Mempool?[](https://docs.alchemy.com/docs/ethereum-transactions-pending-mined-dropped-replaced#what-is-a-mempool)

A mempool, or memory pool, is a [collection of pending transactions waiting for validation from a node](http://www.alchemy.com/overviews/what-is-a-mempool) before they are committed to a new block on the blockchain. Put simply, the mempool is a staging area for unconfirmed transactions in a node. Every blockchain node in the network has a mempool, and they all intercommunicate to share information about the latest pending transactions.

Mempools exist because only ~200 transactions can be confirmed per block, which are mined about once every 15 seconds.

As a result, pending transactions are broadcasted throughout the entire network of mempools with an associated gas price (i.e. the gas fees that the sender is willing to pay to complete their transaction). When a block is mined, the ~200 pending transactions with the highest gas prices are confirmed onto the blockchain by the node that mines the latest block.

___
Type: #subtopic 
Topics: [[Blockchain]], [[MEV]]


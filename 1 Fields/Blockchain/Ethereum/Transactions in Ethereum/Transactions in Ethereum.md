Transactions are cryptographically signed instructions from accounts. 

Ethereum transactions fall into 3 categories:

1. Simple Transfer - value is sent from one public address to another address.
   
2. Deploy a smart contract - whenever a smart contract is deployed on the blockchain, it creates a transaction.
   
3. Execute a smart contract - if an address would like to send funds or data to a smart contract address.


### Transaction lifecycle

1. A user creates a transaction and signs using their private key.
   
2. A node receives the transaction and stores it in the mempool.
   
3. While in the mempool, the node performs validation tests on the transaction. If these tests are passed, the transaction status is moved to 'Pending'.
   
4. The node broadcasts the pending transaction to all other nodes on the network to add the transaction to their own mempools.

5. A miner will then include the transactions with the highest gas fees for the next block.


___
Type: #subtopic 
Topics: [[Blockchain]], [[Ethereum]]


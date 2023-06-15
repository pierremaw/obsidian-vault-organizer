When we have an Externally Owned Account and we want to communicate with the Ethereum Network we broadcast a **transaction**. Inside this transaction we can choose to send **data** which is bytecode intended to interact with the EVM.

> 📖 If we don't send data then there's no intention to interact with the EVM. This is the case for simple ether transfers from one address to another.

The data, often referred to as the **calldata**, is used to pass a **message** into the EVM. It will target a specific contract account (could be either a `contract` or `library` in Solidity terms) which may also make calls to another contract account. Every time a contract account calls into another contract account it forms a message. This message includes its sender address, the targeted function signature, and the amount of wei sent.

In Solidity we have access to these message through global variables:

-   **msg.data** (`bytes`) - the complete calldata
-   **msg.sender** (`address`) - the address sending the message
-   **msg.sig** (`bytes4`) - the targeted function signature
-   **msg.value** (`uint`) - the amount of wei sent

> 💭 Wondering why the msg.sig is 4 bytes? This value is actually the first four bytes of the keccak256 hash of the function signature. It provides a way to uniquely identify (and target) the functions on a smart contract without worrying about how long the function signature is. Otherwise you could potentially store a reallyLongNameForAFunction and the calldata would need to store all of this information to invoke that function! 😱
___
Type: #subtopic 
Topics: [[Blockchain]], [[Ethereum]]


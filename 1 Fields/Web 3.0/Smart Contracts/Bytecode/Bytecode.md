Bytecode is the information that our Solidity code gets “translated” into. It contains instructions to the computer in binary. Each instruction step is an operation which is referred to as “[opcodes](https://github.com/crytic/evm-opcodes),” which are typically one-byte (eight-bits) long. This is why they’re called “bytecode”—one-byte opcodes.

Every line of code that is written gets broken down into opcodes so that the computer knows exactly what to do when running our code.

There are two types of bytecode:

1.  **Creation time bytecode** - is executed only once at deployment, contains the `constructor`
2.  **Run time bytecode** - is stored on the blockchain as permanent executable

**Transaction Receipt**

![[Bytecode.png]]

As in the script above, we provide the ABI to ethers. Once ethers has the contract's ABI, we can make a call to the [`Counter`](https://goerli.etherscan.io/address/0x5F91eCd82b662D645b15Fd7D2e20E5e5701CCB7A#code) smart contract's `inc()` function. Like the image above shows, the front-end library then translates and delivers any requests using the ABI. Once the transaction is successfully sent and validated on the Ethereum network, a **receipt** is generated containing logs and any gas used.

___
Type: #subtopic 
Topics: [[Web 3.0]], [[Smart Contracts]]


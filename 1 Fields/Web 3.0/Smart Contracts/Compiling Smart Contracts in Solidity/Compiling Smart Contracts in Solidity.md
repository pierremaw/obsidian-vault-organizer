Compiling smart contracts produces two important artifacts: - the **ABI** representing the public interface of the contract - the **bytecode** representing the program executable that actually lives on the blockchain

If you want to interact with a smart contract, two main pieces are needed: the ABI and the deployed contract's address.

For example, using the ethers.js [Contract](https://docs.ethers.org/v5/api/contract/contract/#Contract) abstraction:

```javascript=
const myContract = new ethers.Contract(ADDRESS_OF_CONTRACT, ABI, SIGNER);
```


___
Type: #subtopic  
Topics: [[Web 3.0]], [[Smart Contracts]]


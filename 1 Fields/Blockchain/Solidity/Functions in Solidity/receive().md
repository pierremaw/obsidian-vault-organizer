The `receive` function is a special payable function that will be invoked when a smart contract receives ether.

```solidity
import "hardhat/console.sol";
contract Contract {
    receive() external payable {
        console.log(msg.value); // 100000
    }
}
```

☝️ You'll notice that `receive` does not use the `function` keyword. This is because it is a _special_ function (like `constructor`). It is the function that runs when a contract is sent ether without any **calldata**.

The receive function must be **external**, **payable**, it cannot receive arguments and it cannot return anything.


| Feature | Description                                                                                                                                                                                                                                                                                                                                                                                                              |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Receive Ether Function      | A contract can have at most one receive function, declared using receive() external payable. This function is executed on a call to the contract with empty calldata and is used for plain Ether transfers. It cannot have arguments, cannot return anything and must have external visibility and payable state mutability. It can be virtual, can override and can have modifiers.                                     |
| Gas Limitations             | The receive function can only rely on 2300 gas being available, leaving little room to perform other operations except basic logging. Writing to storage, creating a contract, calling an external function which consumes a large amount of gas and sending Ether consume more gas than the 2300 gas stipend.                                                                                                           |
| Exception Handling          | When Ether is sent directly to a contract but the receiving contract does not define a receive Ether function or a payable fallback function, an exception will be thrown, sending back the Ether. A contract without a receive Ether function can receive Ether as a recipient of a coinbase transaction or as a destination of a selfdestruct, but it cannot react to such transfers and thus also cannot reject them. |
| Recommended Practices       | Using payable fallback functions for receiving Ether is not recommended, since the fallback is invoked and would not fail for interface confusions on the part of the sender. For receiving Ether, it is recommended to implement a receive Ether function.                                                                                                                                                              |


___
Type: #microtopic 
Topics: [[Blockchain]], [[Solidity]], [[Functions in Solidity]]


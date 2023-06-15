When contract `A` delegates call to contract `B`, `B`'s code will be executed inside contract `A`. This will update state variables and Ether balance inside contract `A` and not `B`.

Delegate call is commonly used to create an upgradable contract.

_Delegatecall_ is identical to [a message call](https://www.alchemy.com/overviews/solidity-call) except that the code at the target address is executed in the context of the calling contract and the values of _msg.sender_ and _msg.value_ are not changed.

_Delegatecall_ has been extremely useful because it serves as the foundation for implementing libraries and modularizing code.

In the example below, when contract B executes the _delegatecall_ function to contract A, the code of contract A is executed but with contract B’s storage.

```

contract A{
  uint8 public num;
  address public owner;
  uint256 public time;
  string public message;
  bytes public data;


  function callOne() public{
      num = 100;
      owner = msg.sender;
      time = block.timestamp;
      message = "Darah";
      data = abi.encodePacked(num, msg.sender, block.timestamp);

  }


contract B{

  uint8 public num;
  address public owner;
  uint256 public time;
  string public message;
  bytes public data;

  function callTwo(address contractAddress) public returns(bool){

      (bool success,) = contractAddress.delegatecall(
          abi.encodeWithSignature("callOne()")
      );
      }
     
}
```

_delegatecall_ affects the state variables of the contract that [calls a function](https://www.alchemy.com/overviews/solidity-functions) with delegatecall. The state variables of the contract that holds the functions that are borrowed are not read or written.

___
Type: #microtopic 
Topics: [[Blockchain]], [[Solidity]], [[Ethereum]], [[Functions in Solidity]]


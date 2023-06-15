**Global variables**: are predefined special variables, that can be used in any scope in a Solidity program. 
**State variables**: are permanently stored in the contract’s storage. They are defined outside any function’s scope.
**Local variables**: are declared inside a function. They are only accessible within the function.

```solidity
pragma solidity ^0.5.0;
contract Local_variables {
   uint state_var; // State variable
   constructor() public {
      state_var = 10;   
   }
   function getResult() public view returns(uint){
      uint local_var1 = 1; // local variable
      uint local_var2 = 2; // local variable
      uint result = a + b; // local variable
      return result; // access the local variable
   }
}
```

___
Type: #microtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Solidity]]


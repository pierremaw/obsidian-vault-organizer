"Read-only input data storage location"

___

Calldata is not stored in memory or storage. It refers to the input data sent along with a function call, and can be read by the function using the "calldata" specifier. The data is read-only and cannot be modified. Once the function call is complete, the calldata is discarded.

Example
```solidity
function foo(bytes calldata _data) public pure returns (bytes32) {
    bytes32 hash = keccak256(_data);
    return hash;
}
```

In this example, the `calldata` specifier is used to indicate that the argument for the `_data` parameter is passed as input to the `foo` function, and is stored in the read-only `calldata` area of memory. The `foo` function then returns the hash of the input data `_data`.

___
Type: #microtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Solidity]], [[Storage location specifier]]


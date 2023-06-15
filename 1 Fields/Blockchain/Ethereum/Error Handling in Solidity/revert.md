| Feature | Description                                                                                                                                                                                                                                                                                                   |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| REVERT opcode               | The main opcode to revert a transaction in the Ethereum Virtual Machine (EVM).                                                                                                                                                                                                                                |
| assert                      | An opcode that is used to check for internal errors in the EVM. Unlike require and revert, assert will always trigger an error and cannot be disabled.                                                                                                                                                        |
| require                     | A function in Solidity that reverts the transaction if its argument evaluates to false. The require function can also take an optional error message to provide more information about why the transaction was reverted.                                                                                      |
| revert                      | A statement in Solidity that provides access to the REVERT opcode without requiring a boolean condition. The revert statement can also take an optional error message. As of Solidity ^0.8.0, revert is a statement and NOT a function, but it can still be used in function form for backward compatibility. |
| Checking for conditions     | Both require and revert can be used to check for all kinds of conditions in Solidity. By checking for conditions, we can ensure that transactions are executed correctly and the state of the contract remains consistent.                                                                                    |
| Custom error messages       | In Solidity, we can call require and revert with custom error messages or strings to provide more information about why a transaction was reverted. This can be useful for debugging and communicating errors to users.                                                                                       |


___
Type: #microtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Solidity]], [[Error Handling in Solidity]]


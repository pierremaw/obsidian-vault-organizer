
| Modifier | Description | Use case |
| --- | --- | --- |
| `calldata` | read-only input parameters | Use for read-only input parameters that are temporary. |
| `memory` | read-write input parameters | Use it when declaring variables (both function parameters as well as inside the logic of a function) that you want stored temporarily⁴. |
| `storage` | permanent storage on blockchain that is read-write. | Use it when defining variables that you want stored permanently on the blockchain³. |

> In Solidity 0.8.0 only arrays, structs, and mappings can have specific data locations.

# Relative Gas Cost
![[Function Parameter Modifers in Solidity-1.png]]



___
Type: #microtopic 
Topics: [[Blockchain]], [[Solidity]], [[Functions in Solidity]]


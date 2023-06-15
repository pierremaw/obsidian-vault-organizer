| Feature | Description                                                                                                                                                                                                                                                     |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| gasLimit                    | The amount of gas required to transfer ETH from one account to another, which is fixed at 21000.                                                                                                                                                                |
| baseFeePerGas               | The max amount of Gwei required per unit of gas used for the transaction to be included in the next block, calculated by the network based on demand. It is also known as gasPrice in some front-end libraries.                                                 |
| maxPriorityFeePerGas        | An extra amount of Gwei per unit of gas beyond the base fee that one is willing to pay to give priority to their transaction to being included in the next block.                                                                                               |
| maxFeePerGas                | The combined (base fee + priority fee) maximum amount of Gwei per unit of gas one is willing to pay to have their transaction included in the next block. Developers should usually leave this value unset and use the default value determined by the network. |

___
Type: #subtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Solidity]]


**Artifacts** contain compiled contract information.

**Artifacts** are the JSON files that are generated during the contract compilation process. 


| Feature | Description                                                                                                                                                                                                                     |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Compilation                 | Artifacts are generated during the contract compilation process and contain all the necessary information about the compiled contracts, including their bytecode, ABI, and other metadata.                                      |
| JSON files                  | Artifacts are JSON files that are saved in the artifacts/ directory in your Hardhat project.                                                                                                                                    |
| ABI                         | Artifacts contain the ABI (Application Binary Interface) for each contract, which describes the functions, events, and data structures that are available to be used by other contracts or applications.                        |
| Bytecode                    | Artifacts contain the bytecode for each contract, which is the low-level machine code that is executed by the Ethereum Virtual Machine (EVM).                                                                                   |
| Tools and plugins           | Artifacts are used by other plugins and tools in the Hardhat ecosystem, such as the hardhat-contract-sizer plugin, which uses the bytecode size information in the artifacts to help you optimize your contracts for gas usage. |
| Deployment                  | Artifacts are used by the hardhat-deploy plugin to deploy your contracts to the blockchain.                                                                                                                                     |
| artifacts.require           | The artifacts.require function allows you to load the compiled contracts from the artifacts directory and interact with them using their ABI.                                                                                   |
| Testing                     | Artifacts are used in testing to help you verify that your contracts are working as expected. You can use the artifacts.require function to load your compiled contracts and test their functionality.                          |
| Debugging                   | Artifacts can be used in debugging to help you diagnose issues with your contracts. You can inspect the bytecode and other metadata in the artifacts to help identify problems.                                                 |

___
Type: #microtopic 
Topics: [[Web 3.0]], [[Web 3 Development]], [[Hardhat]]


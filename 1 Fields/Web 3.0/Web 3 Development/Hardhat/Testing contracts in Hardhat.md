| Feature          | Description                                                                                                                                                                           |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Initial Setup                        | Initializing a project and setting up the testing environment with recommended tools: ethers, Mocha, Chai, and Hardhat Network Helpers.                                               |
| Simple Test                          | A basic test for verifying the correct behavior of a smart contract function, using expect function from Chai to write the assertions.                                                |
| Testing a Function that Reverts      | Testing a smart contract function that reverts with specific error messages under certain pre-conditions using the .to.be.revertedWith matcher from the Hardhat Chai Matchers plugin. |
| Manipulating the Time of the Network | Simulating the passage of time on the blockchain network for testing smart contract functions that depend on time.                                                                    |
| Using a Different Address            | Testing smart contract functions that require a specific address to be called by, by using a different account to verify that the transaction fails.                                  |
| Using Fixtures                       | Setting up a chain to some desired state using fixtures to speed up testing and avoid duplication of code.                                                                            |
| Measuring Code Coverage              | Using the Solidity-coverage plugin to measure the test coverage in a project.                                                                                                         |
| Using the Gas Reporter               | Using the Hardhat-gas-reporter plugin to get metrics of how much gas is used based on the execution of tests.                                                                         |
| Running Tests in Parallel            | Running tests in parallel mode to speed up testing, but with some limitations to consider.                                                                                            |

___
Type: #microtopic 
Topics: [[Web 3.0]], [[Web 3 Development]], [[Hardhat]]


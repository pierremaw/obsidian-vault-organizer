| Feature        | Description                                                                                   |
|------------------------------------|-----------------------------------------------------------------------------------------------|
| Task                               | A JavaScript async function used for automation in Hardhat. A Hardhat task gets access to the Hardhat Runtime Environment              |
| Metadata                           | Used by Hardhat for argument parsing, validation, and help messages.                          |
| Hardhat Runtime Environment        | Provides configuration and programmatic access to tasks and plugins.                          |
| Built-in tasks                     | Default tasks in Hardhat that use the same APIs available to users.                           |
| @nomicfoundation/hardhat-toolbox   | A package that includes the ethers.js library to interact with contracts.                     |
| hardhat.config.js                  | Configuration file for defining tasks.                                                        |
| Simple tasks                       | Created in the configuration file with the Hardhat Config API.                                |
| Complex tasks                      | Code can be split into several files and required from the configuration file.                |
| Creating tasks through plugins     | Can be created from a separate npm package.                                                   |
| Parsing parameters                 | Hardhat handles validation, parsing, and help messages for parameters.                        |
| Positional and variadic parameters | Must follow certain restrictions to avoid exceptions being thrown.                            |
| Type validations                   | Hardhat converts CLI strings into desired types and prints error messages if it fails.        |
| Overriding tasks                   | Can customize and extend built-in and plugin-provided tasks.                                  |
| runSuper                           | Calls the task's previously defined action when overriding tasks.                             |
| Subtasks                           | Multiple small and focused tasks that call each other for easier extension and customization. |

___
Type: #microtopic 
Topics: [[Web 3.0]], [[Web 3 Development]], [[Hardhat]]


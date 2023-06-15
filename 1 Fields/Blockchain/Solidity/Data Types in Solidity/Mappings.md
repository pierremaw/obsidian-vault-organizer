Mappings are user-defined data types that store key-value pairs. Mappings can only be stored in contract storage and are useful for quickly accessing associated data.

| Feature | Description                                                                                                                                                                                                                                         |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Mapping Definition          | A mapping is defined using the mapping keyword followed by the data type of the key and the data type of the value that is being mapped. For example, mapping (uint => string) public myMapping; creates a mapping from uint keys to string values. |
| Mapping Initialization      | Mappings can be initialized using the constructor function. For example, myMapping[1] = "apple"; would initialize the value of the myMapping mapping for key 1 to be the string "apple".                                                            |
| Mapping Access              | To access a value in a mapping, you use the key in square brackets like an array. For example, myMapping[1] would return the string "apple" if it was previously initialized.                                                                       |
| Mapping Keys                | The keys in a mapping must be of a fixed-size data type and cannot be dynamically sized. Examples of valid key types are uint, address, and bytes32.                                                                                                |
| Mapping Values              | The values in a mapping can be of any data type, including custom structs.                                                                                                                                                                          |
| Mapping Storage             | Mappings are stored in the contract's storage and are therefore more expensive to use than memory or stack variables.                                                                                                                               |
| Mapping Iteration           | Mappings cannot be iterated over like arrays or lists in other programming languages. The only way to access all the keys and values in a mapping is to keep track of them separately in a separate data structure.                                 |
| Mapping Default Values      | By default, all values in a mapping are set to their default value when the contract is deployed. For example, if the value type is uint, all values in the mapping will be initialized to 0.                                                       |

___
Type: #microtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Solidity]], [[Data Types in Solidity]]


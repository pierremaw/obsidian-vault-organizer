Enums are a user-defined data type used to create a set of 'values' that can be assigned to a variable.

| Feature | Description                                                                                                                                                                                                                                          |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Enum            | Enums are a user-defined data type. They allow a developer to create a group of related constants that can be assigned to a variable.                                                                                                    |
| Conversion      | Enums can be converted explicitly to and from all integer types, but implicit conversion is not allowed. The conversion from integer to enum checks at runtime that the value lies inside the range of the enum, otherwise, it causes a Panic error. |
| Range           | Enums cannot have more than 256 members, and the default value when declared is the first member. The options are represented by subsequent unsigned integer values starting from 0.                                                                 |
| Declaration     | Enums can be declared inside or outside of contracts, but require at least one member. Enum constants can also be given values, which can be either integer literals or other constants.                                                             |
| Access          | Enum values are accessed using the dot notation on the enum type, e.g. ActionChoices.GoLeft.                                                                                                                                                         |
| Usage           | Enums can be used to create lists of options, such as directions or states, to be selected from in a contract. They can also be used to make contracts more readable and easier to understand.                                                       |


___
Type: #microtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Solidity]], [[Data Types in Solidity]]


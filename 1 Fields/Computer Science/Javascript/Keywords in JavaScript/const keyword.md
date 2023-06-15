| Feature | Description                                                                                                                                                                                                                                                       |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| const                       | A keyword in JavaScript that declares a constant variable that cannot be reassigned a new value.                                                                                                                                                                  |
| Block Scope                 | Variables declared with const are block-scoped, which means they are only accessible within the block they are declared in (including any nested blocks).                                                                                                         |
| Primitive Data Types        | const can be used to declare constants for primitive data types like numbers, strings, and booleans.                                                                                                                                                              |
| Reference Data Types        | const can also be used to declare constants for reference data types like objects and arrays. While the variable itself cannot be reassigned, the properties of the object or elements of the array can still be modified.                                        |
| Immutability                | const creates an immutable binding, which means that the variable cannot be reassigned a new value. However, this does not mean the value itself is immutable. For example, an object declared with const can still have its properties modified.                 |
| Good Practice               | Using const to declare variables that are not intended to be reassigned can improve code readability and reduce the potential for errors.                                                                                                                         |
| Temporal Dead Zone (TDZ)    | Variables declared with const are hoisted to the top of their block scope, but are not initialized until they are assigned a value. Accessing a const variable before it is initialized results in a ReferenceError and is known as the temporal dead zone (TDZ). |


___
Type: #microtopic 
Topics: [[Computer Science]], [[JavaScript]], [[Keywords in JavaScript]]


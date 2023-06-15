| Feature                  | Base Functions                                                                             | Derived Functions                                                                                                                                         |
| ------------------------ | ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Definition               | Functions that are defined in a contract without any inheritance.                          | Functions that are inherited from a base contract and are modified or extended in a derived contract.                                                     |
| Polymorphism             | Base functions can be made polymorphic using the virtual keyword.                          | Derived functions that override base functions must use the override keyword and have the same name and signature as the base function to be polymorphic. |
| Visibility               | Base functions can have any visibility, including public, private, internal, and external. | Derived functions can have any visibility, including public, private, internal, and external.                                                             |
| Modifiers                | Base functions can have any number of modifiers applied to them.                           | Derived functions can have any number of modifiers applied to them, but cannot override or remove modifiers applied to the base function.                 |
| Access to Base Functions | Derived contracts can call base functions using the super keyword.                         | Base functions cannot call derived functions.                                                                                                             |
| Error Handling           | Base functions can use the revert() and require() functions to handle errors.              | Derived functions can use the revert() and require() functions to handle errors.                                                                          |
| Shadowing                | State variable shadowing is not allowed in base functions.                                 | State variable shadowing is not allowed in derived functions.                                                                                             |

___
Type: #microtopic 
Topics: [[Blockchain]], [[Solidity]], [[Functions in Solidity]]


Function modifiers are keywords that can be added to function definitions to modify their behavior.

| Feature                            | Description                                                                                                                                                                                                              |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Modifiers                          | Modifiers are used to change the behavior of functions in a declarative way. They are inheritable properties of contracts and can be overridden by derived contracts if marked virtual.                                  |
| Function visibility                | Solidity has four types of function visibility: public, internal, private, and external.                                                                                                                                 |
| State variable visibility          | Solidity has three types of state variable visibility: public, internal, and private.                                                                                                                                    |
| Multiple modifiers                 | Multiple modifiers are applied to a function by specifying them in a whitespace-separated list and are evaluated in the order presented.                                                                                 |
| Modifiers and function arguments   | Modifiers cannot implicitly access or change the arguments and return values of functions they modify. Their values must be passed explicitly at the point of invocation.                                                |
| Explicit returns in modifiers      | Explicit returns from a modifier or function body only leave the current modifier or function body.                                                                                                                      |
| Placeholder statement in modifiers | The _ symbol is used as a placeholder in function modifiers to denote where the body of the function being modified should be inserted.                                                                                  |
| Modifiers with return statements   | Modifiers with return statements do not affect the values returned by the function. The modifier can choose not to execute the function body at all, in which case the return variables are set to their default values. |
| Arbitrary expressions in modifiers | Arbitrary expressions are allowed for modifier arguments, and symbols visible from the function are visible in the modifier.                                                                                             |

___
Type: #microtopic 
Topics: [[Blockchain]], [[Solidity]], [[Ethereum]], [[Functions in Solidity]]


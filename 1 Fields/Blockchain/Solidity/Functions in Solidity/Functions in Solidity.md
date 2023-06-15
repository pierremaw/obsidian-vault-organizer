A function is a reusable code piece. Functions are usually defined inside a contract, but they can also be defined outside of contracts.

### Format
```Solidity
function function_name(type1 par1, type2 par2) 
visibility other_modifiers returns (return_variables) 
{
    // Function body
}
```

| Feature                  | Description                                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------------- |
| Solidity Functions       | Self-contained modules of code to perform tasks                                             |
| Solidity Function Syntax | Function keyword, name, parameters, visibility, modifiers, returns                          |
| Special Functions        | Getter, receive, fallback                           |
| Getter Function          | State variables defined as public have a getter                                             |
| Receive Ether Function   | A contract can have at most one receive function                                            |
| Fallback Function        | External function without name, args, or returns                                            |
| Function Overloading     | Multiple definitions for a function name                                                    |
| Function Visibility      | Control which entities can call functions                                                   |
| Public                   | Function can be called from the main contract, derived contracts, and third-party contracts |
| Internal                 | Function can only be called from the main contract and derived contracts                    |
| Private                  | Function can only be called from the main contract                                          |
| External                 | Function can only be called by third-party contracts                                        |
| Pure Functions           | No state variable is changed or read                                                        |
| View Functions           | Read-only functions, cannot alter state variables                                           |



___
Type: #subtopic 
Topics: [[Blockchain]], [[Solidity]]


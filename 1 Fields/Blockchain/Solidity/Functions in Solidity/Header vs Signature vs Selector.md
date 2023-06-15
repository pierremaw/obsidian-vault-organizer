| Term               | Description                                                                                                                                  |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Function Header    | The function header is the function's first line. The header specifies the function's name, parameters, visibility, modifiers, and returns.  |
| Function Signature | A combination of a function name and the types of parameters it takes, combined together as a string with no spaces                          |
| Function Selector  | To get a function's selector, take the function signature, hash it with keccack256, then take the first 4 bytes. |

# Example

**Function definition**
```
function transfer(address sender, uint256 amount) public {
	// Some code here 
}
```

**Function header**
```
function transfer(address sender, uint256 amount) public
```

**Function signature**
```
transfer(address,uint256)
```

**Function selector**
```
bytes4(keccak256(bytes(function_signature)))
```

___
Type: #microtopic 
Topics: [[Blockchain]], [[Solidity]], [[Functions in Solidity]]


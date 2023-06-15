`__init__` is a special function that is executed only once when the contract is deployed.

It is commonly used to initialize state variables.

Format
```Vyper

nums: DynArray[uint256, 3]

@external
def __init__():
	self.nums.append(11)
	self.nums.append(22)
	self.nums.append(33)

```
___
Type: #microtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]], [[Functions in Vyper]]


[Chainlink Guide](https://docs.chain.link/getting-started/deploy-your-first-contract/)
# Write the smart contract

## Declare the compiler version

#### Solidity
```
/// SPDX-License-Identifier: MIT
pragma solidity 0.8.10;
```

#### Vyper
```
# @version ^0.3.7
```

## Declare state variables (public and/or private)

#### Solidity
```
/// SPDX-License-Identifier: MIT
pragma solidity 0.8.10;

contract Counter {
    
    uint public number;
    uint private number_private;

	constructor {
		number = 1
		number_private = 1
	}

    function increment() external {

        number += 1;
        number_private += 1;

    }

}

```

#### Vyper
```
# publis state variable
owner: public(address)
bar: public(bool)

# private state variable
foo: uint256
```

### Define the constructor function

#### Solidity
```
contract SolidityTest {
   uint public storedData ;    /// State variable that is public
   
   constructor() public {      /// Constructor function
      storedData = 10;         /// Using State variable
   }
}
```

#### Vyper
```
# publis state variable
owner: public(address)
bar: public(bool)

# private state variable
foo: uint256

@external
def __init__():
    self.owner = msg.sender
    self.foo = 123
    self.bar = True

```

### Define other functions

#### Solidity
```

```


#### Vyper
```

```

# Compile the smart contract


# Deploy the smart contract


# Interact with functions defined in the smart contract


___
Type: #subtopic 
Topics: [[Web 3.0]], [[Smart Contracts]]


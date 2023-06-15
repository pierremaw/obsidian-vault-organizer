When contract `A` delegates call to contract `B`, `B`'s code will be executed inside contract `A`. This will update state variables and Ether balance inside contract `A` and not `B`.

Delegate call is commonly used to create an upgradable contract.


___
Type: #microtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]], [[Functions in Vyper]]


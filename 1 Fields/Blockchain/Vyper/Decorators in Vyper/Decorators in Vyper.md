A function modifer that alters another function's behavior 

All functions must include one [visibility](https://docs.vyperlang.org/en/v0.3.7/control-structures.html?highlight=decorators#function-visibility) decorator (`@external` or `@internal`). The remaining decorators are optional.

___

# Visibility Decorators

## [[@external decorator]]

Function can only be called externally

## [[@interal decorator]]

Function can only be called within current contract

# Mutability Decorators

## Default Mutability Decorator
Functions default to `@nonpayable` when no mutability decorator is used.

## [[@pure decorator]]

`@pure` functions cannot read state or global variables. Functions marked with `@pure` can only call other `@pure` functions.

## [[@view decorator]]

`@view` functions can read state variables and global variables.

`@view` functions **can** call other internal functions that are:
- `@pure` functions
- `@view` functions

`@view` functions **cannot** call functions thate are mutable functions:
- `@payable` functions 
- `@nonpayable` functions.

## [[@payable decorator]]
Function is able to receive Ether. 

## [[@nonreentrant(unique_key)]]

Function cannot be called back into during an external call

___
Type: #subtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]]


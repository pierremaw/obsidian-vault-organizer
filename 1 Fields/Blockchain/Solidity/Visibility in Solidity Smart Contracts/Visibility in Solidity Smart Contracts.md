# State Variable Visibility Modifiers

## `public`

`public` state variables can be accessed by the main contract, derived contracts, and third party contracts.

## `internal`

Internal state variables can be accessed by the main contract and in derived contracts.

**State variables are `internal` by default.**

## `private`

Private state variables are only visible for the main contract they are defined in.


# Function Visibility Modifiers

## `public`

`public` functions can be accessed by the main contract, derived contracts, and third party contracts .

**A function is `public` by default.**

## `external`

`external` functions an only be called by third party contracts.

## `internal`

`internal` functions can be called by the main contract and derived contracts.

## `private`

`private` functions can only be called by the main contract in which it was specified.


___
Type: #subtopic  
Topics: [[Blockchain]], [[Ethereum]], [[Solidity]]


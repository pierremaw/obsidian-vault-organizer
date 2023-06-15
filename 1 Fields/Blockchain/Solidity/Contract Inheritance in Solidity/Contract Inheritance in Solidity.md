In Solidity, the terms "inheritance" and "derived contracts" are used interchangeably to describe the relationship between a base contract and a child contract. Both terms refer to the mechanism by which a child contract can inherit functions and state variables from a parent or base contract.

# What gets inherited?

When a child contract inherits from a parent or base contract, **it gains access to all the public and internal functions and state variables of the parent contract**. The child contract can then extend, override, or implement additional functions or state variables as needed.

> However, it's important to note that if a function or state variable in the parent contract is marked as private, it cannot be accessed or manipulated by the child contract. Private functions and variables are only accessible within the scope of the contract in which they are defined.


# `is` keyword

In Solidity, you can use the `is` keyword to indicate that a child contract is inheriting from a parent or base contract. For example:

```
contract Parent {
  uint public x;

  function foo() public pure returns (uint) {
    return 42;
  }
}

contract Child is Parent {
  function bar() public view returns (uint) {
    return x;
  }
}

```

In the above code, the `Child` contract inherits from the `Parent` contract using the `is` keyword. As a result, the `Child` contract gains access to the `x` state variable and the `foo()` function defined in the `Parent` contract.

So, to summarize, both inheritance and derived contracts refer to the same mechanism in Solidity by which a child contract can inherit functions and state variables from a parent or base contract.
___
Type: #subtopic 
Topics: [[Blockchain]], [[Solidity]]


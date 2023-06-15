Smart contracts are computer programs that run on blockchains. Programs consist of functions and data (also known as variables or parameters) that functions operate on. The data that functions use need to be stored somewhere in the computer’s memory. In this case the computer is the EVM.

# What is a Solidity smart contract?

A Solidity smart contract is a program [written in Solidity](https://www.alchemy.com/overviews/solidity), deployed to the Ethereum blockchain, and executed in the Ethereum Virtual Machine (EVM). Ethereum stores the smart contract code and data (its state) at a designated address.

When predetermined conditions are met, the program, or smart contract, stored on the blockchain is executed without the need of an intermediary. Smart contracts are, in other words, programs which govern the behavior of accounts within the Ethereum state. 

You can write smart contracts in Solidity or any other EVM-compatible programming language. They must be compiled into bytecode first to be EVM compatible.

Solidity is an object-oriented, high-level language for writing smart contracts. Smart contracts written in Solidity can be used for various purposes like voting, crowdfunding, blind auctions, and multi-signature wallets.

# How do smart contracts work?

Smart contracts are programs stored on the blockchain. A smart contract fortifies agreements between various parties in code and enforces rules automatically when pre-conditions are met. This means that all parties involved in the smart contract are immediately certain of the outcome, without time lost or involvement of a third party. Smart contracts can also automate workflows to trigger the next event upon execution.

Smart contracts that follow the [ERC20 standard](https://www.alchemy.com/overviews/erc20-solidity) are considered ERC20 tokens. ERC20 tokens allow for the transfer of tokens between holders.

# What are the properties of Solidity smart contracts?

Smart contracts are by nature, immutable and deterministic. This means that once a smart contract is deployed or built on Ethereum, it will never cease to exist unless conditions which trigger a self-destruct have been programmed within it. The code will always execute on the conditions it has been programmed to. 

Additionally, smart contracts are deterministic since each network node is able to produce the same result when the same input is given for a method. Should different nodes arrive at different outputs on execution of the smart contract, the consensus protocol is violated and the smart contract is rendered unusable.

Also, smart contracts are permissionless, which means anyone in possession of ETH and has access to the internet is able to deploy a smart contract on Ethereum. 

Finally, smart contracts are composable. This means that you can use smart contracts from other projects as building blocks for your project. Smart contracts can be thought of as open APIs where users do not need to write their own smart contract to become a dApp developer, users just need to know [how to interact with them](https://docs.soliditylang.org/en/v0.8.13/abi-spec.html).

# Solidity Smart Contract Syntax

While there are many resources available to help you [get started learning Solidity](https://www.alchemy.com/overviews/learn-solidity), this section will outline the syntax used to write Solidity smart contracts. 

## 1. Contracts

Contracts in Solidity are similar to classes in object-oriented languages. Each contract can contain declarations of State Variables, Functions, Function Modifiers, Events, Errors, Struct Types and Enum Types. In this article we will discuss Constructors, State Variables and Integer Variables in further detail. Furthermore, contracts can inherit from other contracts.

There are also special contracts called libraries and [interfaces](https://www.alchemy.com/overviews/solidity-interface). 

## 2. Semantic Versioning

Solidity, like most softwares, uses semantic versioning. This means there are no big changes unless you are updating a major version. You can refer to the main breaking changes introduced to each Solidity version on the docs. The most updated version of Solidity is **v0. 8.16**, as of August 2022.

## 3. Constructor

A constructor is called only once during deployment, or contract creation. A constructor is an [optional function](https://www.alchemy.com/overviews/solidity-functions) declared with the constructor keyword and allows you to run contract initialization code. 

Before the constructor code is executed, state variables are initialized to their specified value if you initialize them inline, or their default value if you do not.

After the constructor has run, the final code of the contract is deployed to the blockchain.

If there is no constructor, the contract will assume the default constructor. 

## 4. State Variables

State variables are variables whose values are stored in contract storage. Each function has its own scope, and state variables should always be defined outside of that scope.

State variables adhere to visibility. You can make state variables public with the [_public_ visibility keyword](https://www.alchemy.com/overviews/solidity-function-visibility), which provides a getter function which other smart contracts can access.

## 5. Modification

In Solidity, [a modifier amends the semantics of a function](https://www.alchemy.com/overviews/solidity-modifier) in a declarative way. In other words, modifiers change the behavior of the function to which they are attached. Modifiers are useful in eliminating code redundancy and can be reused to check for the same condition in multiple functions within a smart contract. 

## 6. Integer variables

There are two types of integer variables in Solidity: [unsigned integers (uint)](https://www.alchemy.com/overviews/solidity-uint), and signed integers (int). A signed integer is a value data type that can store negative and positive values. An unsigned integer, on the other hand, has no sign and therefore is a value data type that must be non-negative.

___
Type: #subtopic  
Topics: [[Blockchain]], [[Ethereum]], [[Solidity]]


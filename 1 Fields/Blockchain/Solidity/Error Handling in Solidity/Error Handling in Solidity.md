**Assert** – is used to check for conditions that should never be possible.  Asserts should always evaluate to true and should never fail.  If it does fail then there is a bug in the code and the assert will use up all gas and the transaction will be rolled back.

Example function:

```javascript
Uint public balance; //state variable

Function deposit (uint _amount) public {
    Uint oldBalance = balance;
    Balance += _amount;
    Assert(balance >= _amount; 
// this assert statement should be true and we should really use require
// the statement below in the require section is correctly used
```

Try it in [Remix](https://remix.ethereum.org/)


**Require** – Is used to evaluate inputs, preconditions and outputs of functions.  If not true solidity with throw an error and fail.  The require statement will accept an optional error message.  If there is a failure it will **NOT** use up all gas.

Example function:

```javascript
Function deposit (uint _amount) public {
    Uint oldBalance = balance;
    Uint newBalance = balance +amount
    Require(newBalance >= oldBalance, “Overflow”); // we need to check the requirement first then update the balance

     Balance += +amount; // after checking our condition then perform adding the amount to the balance
     Assert(balance>= +amount; // this assert statement should be true
```

Try it in [Remix](https://remix.ethereum.org/)


**Revert** – Is similar to require but only takes one argument which is the error message.  Revert might be better to use when the condition to check is complex.

Example function:

```javascript
Function withdraw (uint _amount) public {
    Uint oldBalance = balance;
    Require(newBalance<= oldBalance, “Overflow”);
    If (balance < _amount) {
    Revert(“underflow) {
    Balance += +amount;
```

Try it in [Remix](https://remix.ethereum.org/)

For more information [read the docs](https://docs.soliditylang.org/en/v0.8.1/control-structures.html?highlight=error%20handling#error-handling-assert-require-revert-and-exceptions).


___
Type: #subtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Solidity]]


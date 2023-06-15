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


___
Type: #microtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Solidity]], [[Error Handling in Solidity]]


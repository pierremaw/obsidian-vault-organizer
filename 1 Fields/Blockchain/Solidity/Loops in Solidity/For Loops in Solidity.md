A loop will run n times where n is the number we pass into the function. There should be an upper bound so it does not run out of gas.

```javascript
uint public count
Function nameLoop(uint n) public {
         For(uint i =0; i < n; i++ ) {
	           Count +=1; //Execute this code in the brace. Increment the counter by 1 every time the for loop runs
          }
```

Try it in [Remix](https://remix.ethereum.org/)

-   Local variable starts at 0
-   While i < n the code will get executed and for every pass we will increment i.
    -   Let’s say we pass in 4. Then the function will run from 0-4 times
        -   0<4 – function executes in braces below statement, then increment i
        -   1<4 – function executes in braces below statement, then increment i
        -   2<4 – function executes in braces below statement, then increment i
        -   3<4– function executes in braces below statement, then increment i
        -   4 is not <4 so loop terminates


___
Type: #microtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Solidity]], [[Loops in Solidity]]




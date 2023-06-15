You can use `for` to iterate through the values of any array variable:
```
foo: int128[3] = [4, 23, 42]
for i in foo:
    ...
```
In the above, example, the loop executes three times with `i` assigned the values of `4`, `23`, and then `42`.

You can also iterate over a literal array, as long as a common type can be determined for each item in the array:
```
for i in [4, 23, 42]:
    ...
```

Some restrictions:
-   You cannot iterate over a multi-dimensional array. `i` must always be a base type.
-   You cannot modify a value in an array while it is being iterated, or call to a function that might modify the array being iterated.
___
Type: #subtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]]


There are 2 ways to loop through an array, using `range` and directly looping through array elements.

A for loop enables you to traverse items in a sequence.

### Traversing an Array with a For Loop

To traverse an array using a for loop in Vyper, you can use the `len` function to get the length of the array, and then use a for loop to iterate over the array.

Here's an example:

```
@external
@pure
def sum(nums: uint256[10]) -> uint256:
    sum_result: uint256 = 0
    for n in nums:
        sum_result += n
        
    return sum_result
```

In this example, we're defining an array `my_array` and using a for loop to iterate over it. We're using the `len` function to get the length of the array, and then using a for loop to iterate over the array and sum the values.


___
Type: #subtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]]


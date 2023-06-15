
## Components

Dynamic arrays in Vyper are composed of two key components:
- **Data type:** Dynamic arrays are specified using the type of the elements they will contain, followed by a pair of square brackets `[]`. For example, `uint256[]` specifies a dynamic array that will contain elements of type `uint256`.

- **Array functions:** Vyper provides several built-in functions for working with dynamic arrays. These include:
    - `Array()`: This function is used to initialize a dynamic array with a given size. For example, `my_array: uint256[] = Array(5)` creates a dynamic array named `my_array` with a size of 5.
    - `append()`: This function is used to add an element to the end of a dynamic array. For example, `append(my_array, 10)` adds the value `10` to the end of `my_array`.
    - `del`: This keyword is used to remove an element from a dynamic array. For example, `del my_array[0]` removes the first element from `my_array`. 

### Workflows

The typical workflows for working with dynamic arrays in Vyper are as follows:

1.  **Declaration**: Declare the dynamic array and specify its data type. For example, `my_array: uint256[]`.
2.  **Initialization**: Initialize the dynamic array using the `Array()` function. For example, `my_array = Array(5)`.
3.  **Accessing elements**: Access elements of the array using their index within the array. For example, `my_array[0]` accesses the first element of the array.
4.  **Modifying elements**: Modify elements of the array using their index within the array. For example, `my_array[0] = 10` modifies the first element of the array to have the value `10`.
5.  **Appending elements**: Append elements to the end of the array using the `append()` function. For example, `append(my_array, 20)` adds the value `20` to the end of `my_array`.
6.  **Removing elements**: Remove elements from the array using the `del` keyword. For example, `del my_array[0]` removes the first element from the array.

### Example

```vyper
nums: DynArray[uint256, 3] # declaration

nums: DynArray[uint256, 3] = [1, 2, 3] # declaration & initialization
```
___
Type: #microtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]], [[Data Structures in Vyper]], [[Arrays in Vyper]]



# Array

An array is a collection of elements. The elements have the same data type. 

## Static Array

In Vyper, arrays are defined by specifying the data type of the elements in the array, followed by the number of elements in the array.

To create a static array in Vyper, you need to declare it. To declare a staticy array you need to specify the data type for the elements in the array. And you need to specifiy the number of elements in the array.

```python
my_array: int128[3] = [1, 2, 3]
```

## Dynamic Array

To create a dynamic array in Vyper, you need to declare it with a data type
```Vyper
dynamic_array: uint256[]
```



# List

A data structure that store elements in a sequence. In Vyper, a list is created using square brackets [] and individual elements are separated using commas.
```python
my_list: int128[] = [1, 2, 3, 4, 5]
```

# Tuple

A tuple is an immutable sequence. The sequence contains items.
```python
my_tuple: (int128, int128, int128) = (1, 2, 3)
```

# Set

A set is a collection of unique elements. In Vyper, a set is created using the `set()` function.
```python
my_set: set(int128) = set([1, 2, 3, 4, 5])
```

# [[Mapping]]

A mapping is a collection of key-value pairs, where the key and the value can be of different data types. In Vyper, mappings are defined by specifying the data type of the key and the value.

```python
# Example of a mapping from addresses to integers
my_mapping: HashMap[address, int128] = {
    0x1234567890123456789012345678901234567890: 42,
    0x0987654321098765432109876543210987654321: 1234
}

```

# Struct

A struct is a custom data type that allows you to define your own data structure. In Vyper, structs are defined by specifying the name of the struct and the fields of the struct.

```python
# Example of a struct representing a person
struct Person:
    name: string
    age: int128

# Example of creating a new person
my_person: Person = Person({name: "Alice", age: 30})
```

___
Type: #subtopic
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]]


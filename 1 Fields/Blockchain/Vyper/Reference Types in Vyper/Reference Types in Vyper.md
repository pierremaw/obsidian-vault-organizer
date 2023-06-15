Reference types are those whose components can be assigned to in-place without copying. For instance, array and struct members can be individually assigned to without overwriting the whole data structure.

> In terms of the calling convention, reference types are passed by value, not by reference. That means that, a calling function does not need to worry about a callee modifying the data of a passed structure.

# Array(Static)
> Fixed-size lists hold a finite number of elements which belong to a specified type.
> 
> Lists can be declared with `_name: _ValueType[_Integer]`.
```
exampleList: int128[3]
```

# Arrays (Dynamic)
> Dynamic arrays represent bounded arrays whose length can be modified at runtime, up to a bound specified in the type. They can be declared with `_name: DynArray[_Type, _Integer]`, where `_Type` can be of value type (except `Bytes[N]` and `String[N]`) or reference type (except mappings).
```
exampleList: DynArray[int128, 3]
```


# Hash Map
> Mappings are [hash tables](https://en.wikipedia.org/wiki/Hash_table) that are virtually initialized such that every possible key exists and is mapped to a value whose byte-representation is all zeros: a type’s [default value](https://docs.vyperlang.org/en/stable/types.html#types-initial). 
> 
> The key data is not stored in a mapping. Instead, its `keccak256` hash is used to look up a value. For this reason, mappings do not have a length or a concept of a key or value being “set”.
> 
> Mapping types are declared as `HashMap[_KeyType, _ValueType]`.
> Mappings are only allowed as state variables.
```

```
# Structs
> Structs are custom defined types that can group several variables.
> 
> Struct types can be used inside mappings and arrays. Structs can contain arrays and other structs, but not mappings.
> 
> Struct members can be accessed via `struct.argname`.
```
# Defining a struct
struct MyStruct:
    value1: int128
    value2: decimal

# Declaring a struct variable
exampleStruct: MyStruct = MyStruct({value1: 1, value2: 2.0})

# Accessing a value
exampleStruct.value1 = 1
```



___
Type: #subtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]]


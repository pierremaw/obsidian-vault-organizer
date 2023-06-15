# Reference Types

Data types that hold values directly in Solidity

## Major Value Types

-   **Boolean**: Represents true or false values
-   **Integer**: Signed and unsigned integers of various sizes
-   **Address**: Ethereum addresses for accounts and contracts
-   **Bytes**: Fixed-length byte arrays
-   **Enum**: User-defined data types with a finite set of values

## Boolean

-   **Keywords**: `bool`, `true`, `false`
-   **Operators**: Logical (`&&`, `||`, `!`) and comparison (`==`, `!=`) operators

## Integer

-   **Keywords**: `int`, `uint`, `int8` to `int256`, `uint8` to `uint256`
-   **Operators**: Arithmetic (`+`, `-`, `*`, `/`, `%`), bitwise, and comparison operators

## String

-   **Keywords**: `int`, `uint`, `int8` to `int256`, `uint8` to `uint256`
-   **Operators**: Arithmetic (`+`, `-`, `*`, `/`, `%`), bitwise, and comparison operators

## Address

-   **Keywords**: `address`, `address payable`
-   **Functions**: `transfer`, `send`, `call`, `delegatecall`, `staticcall`
-   **Conversion**: Convert between `address` and `address payable`

## Bytes

-   **Keywords**: `bytes1` to `bytes32`
-   **Access**: Access individual bytes using their index
-   **Conversion**: Convert between `bytes` and other types

## Enum

-   **Declaration**: Define an enum using the `enum` keyword
-   **Instantiation**: Assign an enum value using the enum type and value
-   **Access**: Retrieve or modify enum values in variables


# References Types

Data types that store references in Solidity

## Major Reference Data Types

-   **Arrays**: Dynamically-sized or fixed-length collections of elements
-   **Mappings**: Key-value pairs for efficient data storage and retrieval
-   **Structs**: User-defined data structures combining multiple variables

## Arrays

-   **Declaration**: Defining an array with the type and size
-   **Instantiation**: Creating an array instance with specific values
-   **Access**: Retrieving or modifying elements using their index

## Mappings

-   **Declaration**: Defining a mapping with key and value types
-   **Assignment**: Storing values associated with unique keys
-   **Access**: Retrieving values using their corresponding keys

## Structs

-   **Declaration**: Defining a struct using the `struct` keyword
-   **Instantiation**: Initializing a struct instance with specific values
-   **Access**: Assigning or retrieving values of struct members

## Storage

-   **Contract Storage**: Reference data types stored persistently in the blockchain
-   **Memory**: Reference data types stored temporarily during contract execution

## Usage Patterns

-   **Data Management**: Organizing complex data structures
-   **Efficient Storage**: Reducing gas costs through optimized data structures
-   **Modularity**: Encapsulating related data for easier maintenance


___
Type: #subtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Solidity]]


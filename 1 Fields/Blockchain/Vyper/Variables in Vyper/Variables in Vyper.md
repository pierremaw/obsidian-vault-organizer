# Variables

Variables in Vyper are used to store values in smart contracts. This guide explains how to use variables in Vyper.

## **Declare a Variable**

To declare a variable in Vyper, you simply need to define a variable in a function. Here is an example:

```
def my_function():
    my_variable: uint256
```

In this example, we have declared a variable called **`my_variable`** of type **`uint256`** within the **`my_function`** function.

## **Initialize a Variable**

Variables in Vyper can be initialized with a default value when they are declared. Here is an example:

```
def my_function():
    my_variable: uint256 = 123
```

In this example, we have declared a variable called **`my_variable`** of type **`uint256`** and initialized it with a value of **`123`**.

## **Modify a Variable**

Variables in Vyper can be modified within a function. Here is an example:

```
def my_function():
    my_variable: uint256 = 123
    my_variable = 456
```

In this example, we have declared a variable called **`my_variable`** of type **`uint256`** and set its value to **`123`**. We then modify the value of **`my_variable`** to be **`456`**.

## **Read a Variable**

Variables in Vyper can be read within a function. Here is an example:

```
def my_function() -> uint256:
    my_variable: uint256 = 123
    return my_variable
```

In this example, we have declared a variable called **`my_variable`** of type **`uint256`** and set its value to **`123`**. We then return the value of **`my_variable`** using the **`->`** notation.


___
Type: #subtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]]


A state variable is a variable that is declared at the contract level and stored permanently on the blockchain.

# State Variable Types

State variables in Vyper can be any valid data type.

# Declaring a State Variable

State variables are decleared outside all functions. They are defined at the top scope level for your contract.
```
# publis state variable
owner: public(address)
bar: public(bool)

# private state variable
foo: uint256
```

In this example, we have declared a state variable called `my_variable` that has the type `uint256`. State variables in Vyper can be of any valid data type.

When a State Variable is declared, it is assigned the [default value](https://docs.vyperlang.org/en/stable/types.html#types-initial) for their type.

## Declearing a Constant State Variable 

If you want to decleare a constant state variable, you have to initialize it with a variable when you declare it:

```
MY_CONSTANT: constant(uint256) = 123
MIN: constant(uint256) = 1
MAX: constant(uint)

```

# Initializing a State Variable

> If a state variable is not a constant state variable, then it can be initialized in the ______init_____ constructor function. 
> 
> When there is a reference to initializing a state variable, it generally referers to using the constructor function to initialize the state varaible.


State variables are accessed via the [self](https://docs.vyperlang.org/en/stable/constants-and-vars.html#constants-self) object.

```Vyper
# @version ^0.3.7

# publis state variable
owner: public(address)
bar: public(bool)
# private state variable
foo: uint256


@external
def __init__():
    self.owner = msg.sender
    self.foo = 123
    self.bar = True

```


# State Variable Modifiers

State variables are variables that are pemanently stored in contract storage.

A state variable modifier is a keyword that modifies a state variable’s behaviour.

## **Public Modifier**

The **`public`** modifier can be used to automatically generate a getter function for a state variable. Here is an example:

```
my_variable: public(uint256) = 123
```

In this example, we have declared a state variable called **`my_variable`** of type **`uint256`** and initialized it with a value of **`123`**.

> The **`public`** modifier indicates that a getter function will be automatically generated for this variable.

### **Using the Getter Function**

The getter function for a **`public`** state variable can be used to retrieve the value of the variable. Here is an example:

```
def get_variable() -> uint256:
    return self.my_variable()
```

In this example, we have defined a function called **`get_variable`** that returns the value of the **`my_variable`** state variable using the automatically generated getter function.

## **Constant Modifier**

The **`constant`** modifier can be used to indicate that a state variable does not change after it has been initialized. Here is an example:

```
MY_CONSTANT: constant(uint256) = 123
```

In this example, we have declared a constant called **`MY_CONSTANT`** of type **`uint256`** and initialized it with a value of **`123`**. The **`constant`** modifier indicates that this value will not change after it has been initialized.




___
Type: #subtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]]


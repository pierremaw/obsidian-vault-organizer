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
Type: #microtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]], [[State Variables in Vyper]]


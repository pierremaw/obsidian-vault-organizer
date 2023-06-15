Vyper is a contract-oriented language that supports various types of variables such as state variables, local variables, and environment variables.

# State Variables

State variables are stored on the Ethereum blockchain and represent the state of the contract. State variables can be declared as public or private.

### Public State Variables

Public state variables can be accessed from outside the contract and are automatically generated with a getter function. You can also create a setter function for a public state variable by defining a function with the same name as the state variable.

Example:

```vyper
contract MyContract:
    my_var: public(int128)

    @external
    def __init__(var: int128):
        self.my_var = var

```

### Private State Variables

Private state variables can only be accessed from within the contract. To declare a private state variable, simply omit the `public` keyword.

Example:

```vyper
contract MyContract:
    my_var: int128

    @external
    def set_var(var: int128):
        self.my_var = var

    @external
    def get_var() -> int128:
        return self.my_var

```

# Name Shadowing

Name shadowing happens when you declare a variable with the same name as another variable. In Vyper, you cannot declare a local variable with the same name as a state variable or a function argument. If you do so, the local variable will shadow the other variable, making it inaccessible.

# Constants

In Vyper, constants are declared using the `constant` keyword. Constants are similar to public state variables, but they cannot be modified after initialization.

Example:

```vyper
contract MyContract: 
	MY_CONST: constant(int128) = 123 
	
	@external 
	def get_const() -> int128: 
		return self.MY_CONST
```

# Environment Variables

Environment variables are predefined global variables that are automatically set by the Ethereum virtual machine. Environment variables include `msg.sender`, `msg.value`, and `block.timestamp`.

Example:

```vyper
contract MyContract:
    @external
    def get_sender() -> address:
        return msg.sender

    @external
    def get_value() -> uint256:
        return msg.value

    @external
    def get_timestamp() -> uint256:
        return block.timestamp

```


___
Type: #subtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]]


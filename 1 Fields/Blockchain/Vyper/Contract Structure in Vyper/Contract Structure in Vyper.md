Vyper contracts are contained within files. Each file contains exactly one contract.

This section provides a quick overview of the types of data present within a contract, with links to other sections where you can obtain more details.

# Version Pragma[](https://docs.vyperlang.org/en/v0.3.7/structure-of-a-contract.html#version-pragma "Permalink to this headline")

Vyper supports a version pragma to ensure that a contract is only compiled by the intended compiler version, or range of versions. Version strings use [NPM](https://docs.npmjs.com/about-semantic-versioning) style syntax.

```
# @version ^0.2.0
```

In the above example, the contract only compiles with Vyper versions `0.2.x`.

# State Variables[](https://docs.vyperlang.org/en/v0.3.7/structure-of-a-contract.html#state-variables "Permalink to this headline")

State variables are values which are permanently stored in contract storage. They are declared outside of the body of any functions, and initially contain the [default value](https://docs.vyperlang.org/en/v0.3.7/types.html#types-initial) for their type.

```
storedData: int128
```

State variables are accessed via the [self](https://docs.vyperlang.org/en/v0.3.7/constants-and-vars.html#constants-self) object.

```
self.storedData = 123
```

See the documentation on [Types](https://docs.vyperlang.org/en/v0.3.7/types.html#types) or [Scoping and Declarations](https://docs.vyperlang.org/en/v0.3.7/scoping-and-declarations.html#scoping) for more information.

# Functions[](https://docs.vyperlang.org/en/v0.3.7/structure-of-a-contract.html#functions "Permalink to this headline")

Functions are executable units of code within a contract.

```
@external
def bid():
    ...
```

Functions may be called internally or externally depending on their [visibility](https://docs.vyperlang.org/en/v0.3.7/control-structures.html#function-visibility). Functions may accept input arguments and return variables in order to pass values between them.

See the [Functions](https://docs.vyperlang.org/en/v0.3.7/control-structures.html#control-structures-functions) documentation for more information.

# Events[](https://docs.vyperlang.org/en/v0.3.7/structure-of-a-contract.html#events "Permalink to this headline")

Events provide an interface for the EVM’s logging facilities. Events may be logged with specially indexed data structures that allow clients, including light clients, to efficiently search for them.

```
event Payment:
    amount: int128
    sender: indexed(address)

total_paid: int128

@external
@payable
def pay():
    self.total_paid += msg.value
    log Payment(msg.value, msg.sender)
```

See the [Event](https://docs.vyperlang.org/en/v0.3.7/event-logging.html#event-logging) documentation for more information.

# Interfaces[](https://docs.vyperlang.org/en/v0.3.7/structure-of-a-contract.html#interfaces "Permalink to this headline")

An interface is a set of function definitions used to enable calls between smart contracts. A contract interface defines all of that contract’s externally available functions. By importing the interface, your contract now knows how to call these functions in other contracts.

Interfaces can be added to contracts either through inline definition, or by importing them from a separate file.

```
interface FooBar:
    def calculate() -> uint256: view
    def test1(): nonpayable
```

```
from foo import FooBar
```

Once defined, an interface can then be used to make external calls to a given address:

```
@external
def test(some_address: address):
    FooBar(some_address).calculate()
```

See the [Interfaces](https://docs.vyperlang.org/en/v0.3.7/interfaces.html#interfaces) documentation for more information.

## Structs[](https://docs.vyperlang.org/en/v0.3.7/structure-of-a-contract.html#structs "Permalink to this headline")

A struct is a custom defined type that allows you to group several variables together:
```
struct MyStruct:
    value1: int128
    value2: decimal
```

See the [Structs](https://docs.vyperlang.org/en/v0.3.7/types.html#types-struct) documentation for more information.
___
Type: #subtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Vyper]]


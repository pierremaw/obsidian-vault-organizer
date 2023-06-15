# Storage

Data stored on the block chain.  State variables will have a memory location of storage.  You do not need to declare “storage” since it is declared outside the function.  Use when you want to create a pointer to deeply nested data (example referencing specific data in array.

User storage user = users[0] – this is a pointer to user 0 in the users array saved on the block chain

# Memory

Short term data not kept on the block chain.  Only used in the function.

User memory user = users[0] – this is a pointer to user 0 in the users array within the function

# Stack
Every variable in a function is placed on the stack.  Don’t need to do anything to declare stack.  If there are too many variables in your function you could get an error saying there are too many variables on the stack

# Calldata
Only available to external or public functions
___
Type: #subtopic 
Topics: [[Blockchain]], [[Solidity]]


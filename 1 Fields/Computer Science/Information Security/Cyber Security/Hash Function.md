A **hash function** is a function which takes an input of any size and turns it into a fixed size output

Let's imagine a hash function that takes an input of any size and returns a fixed 32 byte output:

![[Hash Function.png]]

These inputs get larger from top to bottom but they always map to an output of 32 bytes. There are many different [algorithms for hash functions](https://en.wikipedia.org/wiki/Hash_function#Hashing_integer_data_types) which could take these inputs and create outputs of fixed sizes.

The specific types of hash functions we are going to focus on are **cryptographic** hash functions. These hash functions need five specific properties. They must be:

-   🔮 **Deterministic** - One specific input always maps to the **same** specific output
-   🎲 **Pseudorandom** - It is not possible to guess the output based on the output of similar inputs
-   ➡️ **One-way** - If someone gives you a new output, you could not determine an input without guessing
-   🏎️ **Fast to Compute** - It must be a quick calculation for a computer
-   💥 **Collision-resistant** - The chance of a collision should be infinitesimally small

With a secure cryptographic hash function you can create a unique, fixed-size representation of an input regardless of its size. For blockchains this feature is critically important for saving space. In many cases blockchains and smart contracts will not need to store an input, they can just store the hash output. Cryptographic Hash Functions will also be super important for the first successful blockchain consensus mechanism we'll talk about: **proof of work**.
___
Type: #microtopic 
Topics: [[Computer Science]], [[Information Security]], [[Cyber Security]], [[Cryptography]]


To make development easier you can use the import statement in your smart contract to reference contracts stored in other locations. This will allow you to use other contracts / files from Remix or GitHub repositories in your contract while developing and testing. This removes the need to copy and paste contract data.

## Using Import in Solidity

### How to import a files from a tab into a smart contract in Remix

-   Example: contract A and contract B are both in Remix but on different tabs
-   Use the following syntax to import one contract into the other in Remix:

**Import “./contractName.sol”;**

This statement imports all data from contractA into the current global scope of contractB.

## Using Import in Solidity

### How to import a files from a tab into a smart contract in Remix

-   Example: contract A and contract B are both in Remix but on different tabs
-   Use the following syntax to import one contract into the other in Remix:

**Import “./contractName.sol”;**

This statement imports all data from contractA into the current global scope of contractB.

![using import in solidity smart contract into remix](https://cryptomarketpool.com/wp-content/uploads/2021/07/import-in-remix.jpg)

Try in [Remix](http://remix.ethereum.org/)

### How to import files from GitHub into a smart contract in Remix

-   Example: contract B is in Remix but the file we want to import is in GitHub
-   Use the following syntax in Remix to import a file from GitHub:

**Import “urlfromgithub”;**

**Make sure you remove https:// from the url.

This statement imports all data from the GitHub URL into the current global scope of contractB.

![using import in solidity smart contracts into remix from github](https://cryptomarketpool.com/wp-content/uploads/2021/07/import-in-remix-github.jpg)

Try in [Remix](http://remix.ethereum.org/)

-   Make sure the Solidity versions of all your smart contract are the same. To find a different version of a contract in GitHub switch the GitHub branch to the same solidity version your contract is using then copy the URL.

![Importing into a Solidity smart contract](https://cryptomarketpool.com/wp-content/uploads/2021/03/image-3.png)

These are the basic methods of using import in Solidity smart contracts.
___
Type: #microtopic 
Topics: [[Blockchain]], [[Ethereum]], [[Solidity]]


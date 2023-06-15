### [Interacting with existing contracts](https://web3py.readthedocs.io/en/v5/examples.html#id10)[](https://web3py.readthedocs.io/en/v5/examples.html#interacting-with-existing-contracts "Permalink to this headline")

In order to use an existing contract, you’ll need its deployed address and its ABI. Both can be found using block explorers, like Etherscan. Once you instantiate a contract instance, you can read data and execute transactions.

```python
# Configure w3, e.g., w3 = Web3(...)
address = '0x1f9840a85d5aF5bf1D1762F925BDADdC4201F988'
abi = '[{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"address","name":"minter_","type":"address"},...'
contract_instance = w3.eth.contract(address=address, abi=abi)

# read state:
contract_instance.functions.storedValue().call()
# 42

# update state:
tx_hash = contract_instance.functions.updateValue(43).transact()
```
___
Type: #microtopic 
Topics: [[Blockchain]], [[Ethereum]], [[1 Fields/Blockchain/Ethereum/Web3.py/Web3.py]]


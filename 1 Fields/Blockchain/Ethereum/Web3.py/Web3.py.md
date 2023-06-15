A Python library for interacting with blockchains.
# Providers[](https://web3py.readthedocs.io/en/v5/overview.html#providers "Permalink to this headline")

Providers are how Web3.py connects to the blockchain. The provider is how web3 talks to the blockchain. Providers take JSON-RPC requests and return the response. This is normally done by submitting the request to an HTTP or IPC socket based server.

The library comes with the following built-in providers:
- `Web3.IPCProvider` for connecting to ipc socket based JSON-RPC servers.
- `Web3.WebsocketProvider` for connecting to ws and wss websocket based JSON-RPC servers.
- `Web3.HTTPProvider` for connecting to http and https based JSON-RPC servers.


```python

>>> from web3 import Web3

# IPCProvider:
>>> w3 = Web3(Web3.IPCProvider('./path/to/geth.ipc'))

# HTTPProvider:
>>> w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

# WebsocketProvider:
>>> w3 = Web3(Web3.WebsocketProvider('ws://127.0.0.1:8546'))

>>> w3.isConnected()
True
```




___
Type: #subtopic 
Topics: [[Blockchain]], [[Ethereum]]


Proof-of-work is the consensus mechanism that allows decentralized networks like Bitcoin and (previously) Ethereum to come to consensus, or agree on things like account balances and the order of transactions. This prevents users from "double spending" their coins and ensures that everyone is following the rules, making proof-of-work-based networks resistant to attack. The consensus mechanism ends up providing security to a blockchain network just because it demands that everyone follow the consensus rules if they want to participate!

In proof-of-work, **mining** is the "work" itself.

## Mining

**Mining** is process of creating a block of transactions to be added to a blockchain.

Here's what the proof-of-work mining algorithm looks like:

1.  Take current block’s block header, add mempool transactions
2.  Append a nonce, starting at nonce = 0
3.  Hash data from #1 and #2
4.  Check hash versus target difficulty (provided by protocol)
5.  If hash < target, puzzle is solved! Get rewarded.
6.  Else, restart process from step #2, but increment nonce


Why do miners expend resources to secure a proof-of-work blockchain network like Ethereum or Bitcoin? In exchange for the large amounts of energy and hardware upkeep required to run mining software, miners receive currency as a reward. If the consensus rules are followed, making a secure network, miners get paid.

___
Type: #subtopic 
Topics: [[Blockchain]], [[Consensus Mechanism]]


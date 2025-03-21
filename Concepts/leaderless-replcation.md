20.03.2025 18:55
Tags: #concept

---
# Leaderless Replication

Other [[database-replication|replication]] techniques, such as [[leader-based-replication|single-leader]] and [[multi-leader-replication|multi-leader]] replication are based on the idea that a client sends a write request to the leader and the database system takes care of copying that write to the other replicas.

Some data storage systems take a different approach, abandoning the concept of a leader and allowing any replica to directly accept writes from clients. In some leaderless implementations, the client directly sends its writes to several replicas, while in others, a _coordinator node_ does this on behalf of the client. However, unlike a leader database, that coordinator does not enforce a particular ordering of writes.

## Handling Node Outages
Imagine a database with three replicas, and one of them is currently unavailable. In a leaderless configuration, _failover_ does not exist. Let’s say that it’s sufficient for two out of three replicas to acknowledge A write: after user has received two _ok_ responses, we consider the write to be successful. The client simply ignores the fact that one of the replicas missed the write.

Now imagine that the unavailable node comes back online, and clients start reading from it. Any writes that happened while the node was down are missing from that node. To solve that, when a client reads from the database, it sends its read requests to several nodes in parallel. Version numbers are used to determine which value is newer.


### Recovering from outages
The replication scheme should ensure that eventually all the data is copied to every replica. Two mechanisms are often used in Dynamo-style datastores:

- _Read Repair:_ When a client makes a read from several nodes in parallel, it can detect any stale responses by comparing version numbers from each response from each replica, writing newer values back to each stale response. This approach works well for values that are frequently read.
- _Anti-Entropy Process:_ Some datastores have a background process that constantly looks for differences in the data between replicas and copies any missing data from one replica to another. Unlike the replication log in leader-based replication, this  process does not copy writes in any particular order, and there may be a significant delay before data is copied.

```ad-warning
Not all systems implement both of these. Note that without an entropy process, values rarely read may be missing from some replicas and have reduced durability.
```

## Quorums
if there are _n_ replicas, every write must be confirmed by _w_ nodes to be considered successful, and we must query at least _r_ nodes for each read.

As long as _w_ + _r_ > _n_, we expect to get an up-to-date value when reading.

In Dynamo-style databases, the parameters _n_, _w_, and _r_ are typically configurable. A common choice is to make _n_ an odd number (typically 3 or 5) and to set _w_ = _r_ = (_n_ + 1) / 2 (rounded up). However, you can vary the numbers as you see fit, for example, a workload with few writes and many reads may benefit from setting _w_ = _n_ and _r_ = 1. This makes reads faster, but has the disadvantage that just one failed node causes all database writes to fail.

The quorum condition allows the system to tolerate unavailable nodes as follows:

- If _w_ < _n_, we can still process writes if a node is unavailable.
- If _r_ < _n_, we can still process reads if a node is unavailable.
- With _n_ = 3, _w_ = 2, _r_ = 2 we can tolerate one unavailable node.
- With _n_ = 5, _w_ = 3, _r_ = 3 we can tolerate two unavailable nodes. 
- With fewer than the required _w_ or _r_ nodes are available, writes or reads return an error.

### Limitations

Even with _w_ + _r_ > _n_, there are likely to be edge cases where stale values are returned. These depend on the implementation, but possible scenarios include:

- If a sloppy quorum is used, the _w_ writes may end up on different nodes than the r reads, so there is no longer a guaranteed overlap between the _r_ nodes and _w_ nodes.
- If two writes occur concurrently, the only safe solution is to merge the writes, and if a winner is picked based on a timestamp, writes can be lost due to [[clock-skew]].
- If a write happens concurrently with a read, the write may be reflected on only some of the replicas. In this case, it’s undetermined whether the read returns the old or the new value.
- If a write succeeded on some replicas but failed on others, and overall succeeded on fewer than _w_ replicas, it not rolled back on the replicas where it succeeded. This means that if a write was reported as failed, subsequent reads may or may not return the value from that write
- If a node carrying a new value fails, and its data is restored from a replica carrying an old value, the number of replicas storing the new value may fall below _w_, breaking the quorum condition.
- Even if everything is working correctly, there are edge cases in which you can get unlucky with the timing,

Thus, although quorums appear to guarantee that a read returns the latest written value, in practice it is not so simple. Dynamo-style databases are generally optimized for use cases that can tolerate _eventual consistency_.
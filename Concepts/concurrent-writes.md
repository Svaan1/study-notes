20.03.2025 20:39
Tags: #concept

---
# Concurrent Writes

←— intro —>
## “Happens-before” relationship and concurrency
Whenever you have two operations A and B, there are three possibilities: either A happened before B, or B happened before A, or A and B are concurrent.

What we need is an algorithm to tell us whether two operations are concurrent or not. If one operation happened before another, the later operation should overwrite the earlier operation, but if the operations are concurrent, we have a conflict that needs to be resolved.

```ad-info
title: Concurrency, time and relativity

For defining concurrency, exact time doesn’t matter: we simply call two operations concurrent if they are both unaware of each other, regardless of the physical time at which they occurred.

Two operations can occur some time apart and still be concurrent, because the network problems prevented one operation from being able to know about the other.
```

### Capturing the “happens-before” relationship
The server can determine whether two operations are concurrent by looking at the version numbers, it does not need to interpret the value itself. The algorithm works as follows:

- The server maintains a version number for every key, increments the version number every time that key is written, and stores the new version number along with the value written.
- When a client reads a key, the server returns all values that have not been overwritten, as well as the latest version number. A client must read a key before writing.
- When a client writes a key, it must include the version number from the prior read, and it must merge together all values that it received in the prior read.
- When the server receives a write with a particular version number, it can overwrite all values with that version number or below, but it must keep all values with a higher version number, because those values are concurrent with the incoming write.

When a write includes the version number from a prior read, that tells us which previous state the write is based on. If you make a write without including a version number, it is concurrent with all other writes, so it will not overwrite anything, it will just be returned as one of the values on subsequent reads.

## Handling Write Conflicts
←– intro —>
### Last write wins
One approach for achieving eventual convergence is to declare that each replica need only store the most “recent” value and allow “older” values to be overwritten and discarded.

Even though the writes don’t have a natural ordering, we can force an arbitrary order on them. For example, we can attach a timestamp to each write, pick the biggest timestamp as the most “recent,” and discard any writes with an earlier timestamp.

LWW achieves the goal of eventual convergence, but at the cost of durability: if there are several concurrent writes to the same key, even if they were all reported as successful to the client, only one of the writes will survive and the others will be silently discarded. _If losing data is not acceptable, LWW is a poor choice for conflict resolution._

The only safe way of using a database with LWW is to ensure that a key is only written once and thereafter treated as immutable, thus avoiding any concurrent updates to the same key.
### Merging concurrently written values
A reasonable approach to merge siblings is to just take the union between the conflicting writes.

If you want to allow deletions however, an item cannot be simply deleted from the database when it is removed, the system must leave a marker with an appropriate version number to indicate that the item has been removed when merging, also called a tombstone.
19.03.2025 20:30
Tags: #concept

---
# Multi Leader Replication

[[leader-based-replication|Leader Based Replication]] has one major downside: there is only one leader, and all writes must go through it.

The natural extension of the leader-based replication model is to allow more than one node to accept writes. Replication still happens in the same way: each node that processes a write must forward that data change to all the other nodes. We call this a _multi-leader_ configuration.

```ad-danger
As multi-leader replication is a somewhat retrofitted feature in many databases, there are often subtle configuration pitfalls and surprising interactions with other database features. For example, autoincrementing keys, triggers, and integrity constraints can be problematic. For this reason, multi-leader replication is often considered dangerous territory that should be avoided if possible
```
## Use Cases
It rarely makes sense to use a multi-leader setup within a single datacenter, because the benefits rarely outweigh the added complexity. However, there are some situations in which this configuration is reasonable.

### Multi-datacenter operation
In a multi-leader configuration, you can have a leader replica in each available datacenter, with a regular leader-follower replication being used, and, between datacenters, each datacenter’s leader replicates its changes to the leaders in other datacenters.

Comparison:

- _Performance_: In the multi-leader architecture, the inter-datacenter network delay is hidden from users by processing every write in the local datacenter and replicating it asynchronously to the other datacenters, which means the perceived performance may be better.
- _Outage Tolerance_: In a multi-leader configuration, each datacenter can continue operating independently of the others, and replication catches up when the failed datacenter comes back online.
- _Network Problems Tolerance_: Traffic between datacenters usually goes over the public internet, which may be less reliable than the local network within a datacenter. A [[leader-based-replication||single-leader]] configuration is very sensitive to problems in this inter-datacenter link, because writes are made synchronously over this link. A multi-leader configuration with asynchronous replication can usually tolerate network problems better: a temporary network interruption does not prevent writes being processed.

Although multi-leader replication has advantages, it also has a big downside: the same data may be concurrently modified in two different datacenters, and those write conflicts must be resolved.

### Clients with Offline Operation

Another situation in which multi-leader replication is appropriate is if you have an application that needs to continue to work while it is disconnected from the internet.

In this case, every device has a local database that acts as a leader and there is an asynchronous multi-leader replication process between the replicas of your data on all of your devices. The replication lag may be hours or even days, depending on when you have internet access available.

From an architectural point of view, this setup is essentially the same as multi-leader replication between datacenters, taken to the extreme: each device is a “datacenter,” and the network connection between them is extremely unreliable. As the rich history of broken calendar sync implementations demonstrates, multi-leader replication is a tricky thing to get right.

### Collaborative editing

We don’t usually think of collaborative editing as a database replication problem, but it has a lot in common with the previously mentioned offline editing use case. When one user edits a document, the changes are instantly applied to their local replica and asynchronously replicated to the server and any other users who are editing the same document.

If you want to guarantee that there will be no editing conflicts, the application must obtain a lock on the document before a user can edit it. If another user wants to edit the same document, they first have to wait until the first user has committed their changes and released the lock. This collaboration model is equivalent to [[leader-based-replication|single leader replication]] with [[transactions|transactions]] on the leader.

However, for faster collaboration, you may want to make the unit of change very small and avoid locking. This approach allows multiple users to edit simultaneously, but it also brings all the challenges of multi-leader replication, including requiring [[conflict-resolution|conflict resolution]].

## Handling Write Conflicts

The biggest problem with multi-leader replication is that write conflicts can occur, which means that conflict resolution is required.

_Example_: Consider a wiki page that is simultaneously being edited by two users, user 1 changes the title of the page from A to B, and user 2 changes the title from A to C at the same time. Each user’s change is successfully applied to their local leader. However, when the changes are asynchronously replicated, a conflict is detected. This problem does not occur in a single-leader database.

In a single-leader database, the second writer would either block and wait for the first write or abort the second write transaction, forcing the user to retry the other write.

But in a multi-leader setup, both writes would be successful, thus the conflict would only be detected asynchronously at some later point in time, too late to ask the user to resolve the conflict.

```ad-warning
You could make the conflict detection synchronous, however, by doing so, you would lose the main advantage of multi-leader replication, being able to allow each replica to accept writes independently. If you want synchronous conflict detection, you might as well just use single-leader replication.
```

### Conflict avoidance
The simplest strategy to deal with conflicts is to avoid them, since many implementations of multi-leader replication handle conflicts very poorly, avoiding conflicts is a frequently recommended approach.

For example, in an application where a user can edit their own data, you can ensure that requests from a particular user are always routed to the same datacenter and use the leader in that datacenter for reading and writing.

However, sometimes you might want to change the designated leader for a record, in this situation, conflict avoidance breaks down, and you have to deal with the possibility of concurrent writes on different leaders.

### Converging toward a consistent state
Consistent state in a leader-based database is easily handled, as the statements are usually ordered, the last write wins. However in a multi-leader configuration there is no defined ordering of writes, so there is no easy value to pick as the final one.

If each replica simply applied writes in the order that it saw the writes, the database would end up in an inconsistent state: the final value would be C at leader 1 and B at leader 2. That is not acceptable, every replication scheme must ensure that the data is eventually the same in all replicas. 

Thus, the database must resolve the conflict in a _convergent_ way, which means that all replicas must arrive at the same final value when all changes have been replicated.

- Give each write a unique ID, pick the write with the highest ID as the _winner_, and throw away the other writes. If a timestamp is used, this technique is known as _last write wins_. Although this approach is popular, it is [[concurrent-writes|dangerously prone to data loss]].
- Give each replica a unique ID, and let writes that originated at a higher-numbered replica always take precedence over writes that originated at a lower-numbered replica. This approach also implies data loss.
- Somehow merge the values together—e.g., order them alphabetically and then concatenate them.
- Record the conflict in an explicit data structure that preserves all information, and write application code that resolves the conflict at some later time (perhaps by prompting the user).

### Custom conflict resolution logic
Most multi-leader replication tools let you write conflict resolution logic using application code. That code may be executed on write or on read.

Note that conflict resolution usually applies at the level of an individual row or document, not for an entire [[transactions|transaction]], each write is still considered separately for the purposes of conflict resolution.

## Multi-Leader Replication Topologies

- _All-to-all:_ Every leader sends its writes to every other leader.
- _Star:_ One designated root node forwards writes to all of other nodes, can be generalized to a tree
- _Circular:_ Each node receives writes form one node and forwards those writes to one other node.

in circular and star topologies, a write may need to pass through several nodes before it reaches all replicas. Therefore, nodes need to forward data changes they receive from other nodes. To prevent infinite replication loops, each node is given a unique identifier, and in the replication log, each write is tagged with the identifiers of all the nodes it has passed through. When a node receives a data change that is tagged with its own identifier, that data change is ignored, because the node knows that it has already been processed.

A problem with circular and star topologies is that if just one node fails, it can interrupt the flow of replication messages between other nodes, causing them to be unable to communicate until the node is fixed. The fault tolerance of a more densely connected topology (such as all-to-all) is better because it allows messages to travel along different paths, avoiding a single point of failure.

On the other hand, all-to-all topologies can have issues too. In particular, some network links may be faster than others, with the result that some replication messages may “overtake” others. To order these events correctly, a technique called [[version-vectors|version vectors]] can be used, however, conflict detection techniques are poorly implemented in many multi-leader replication systems.
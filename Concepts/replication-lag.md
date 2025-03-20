19.03.2025 20:00
Tags: #concept

---
# Replication Lag

In a _read-scaling_ architecture, you can increase the capacity for serving read-only requests simply by adding more followers. However, this approach only realistically works with asynchronous replication—if you tried to synchronously replicate to all followers, a single node failure or network outage would make the entire system unavailable for writing. And the more nodes you have, the likelier it is that one will be down, so a fully synchronous configuration would be very unreliable.

Unfortunately, if an application reads from an _asynchronous_ follower, it may see outdated information if the follower has fallen behind. This leads to apparent inconsistencies in the database: if you run the same query on the leader and a follower at the same time, you may get different results, because not all writes have been reflected in the follower. This inconsistency is just a temporary state, if you stop writing to the database and wait a while, the followers will eventually catch up and become consistent with the leader. For that reason, this effect is known as [[consistency-models|eventual consistency]].
## Anomalies
Communications between replicated systems can and will eventually fall behind, and when te lag is large, the inconsistencies it introduces are not just a theoretical issue but a real problem for applications.
### Reading Your Own Writes

_Read-after-write consistency_, also known as _read-your-writes consistency_. This is a guarantee that if the user reloads the page, they will always see any updates they submitted themselves. It makes no promises about other users, it only reassures the user that their own input has been saved correctly.

Hoe can read-after-write consistency be implemented in a system with leader-based replication? There are many possible techniques:

- When reading something that the user may have modified, read it from the leader; otherwise, read it from a follower. This requires that you have some way of knowing whether something might have been modified, without actually querying it. Thus, a simple rule is: always read the user’s own profile from the leader, and any other users’ profiles from a follower.
- If most things in the application are potentially editable by the user, that approach won’t be effective, as most things would have to be read from the leader (negating the benefit of read scaling). In that case, other criteria may be used to decide whether to read from the leader. For example, you could track the time of the last update and, for one minute after the last update, make all reads from the leader. You could also monitor the replication lag on followers and prevent queries on any follower that is more than one minute behind the leader.
- The client can remember the timestamp of its most recent write—then the system can ensure that the replica serving any reads for that user reflects updates at least until that timestamp. If a replica is not sufficiently up to date, either the read can be handled by another replica or the query can wait until the replica has caught up.
- If your replicas are distributed across multiple datacenters (for geographical proximity to users or for availability), there is additional complexity. Any request that needs to be served by the leader must be routed to the datacenter that contains the leader.

Another complication arises when the same user is accessing your service from multiple devices, for example a desktop web browser and a mobile app. In this case you may want to provide _cross-device_ read-after-write consistency, in this case there are some additional issues to consider:

- Approaches that require remembering the timestamp of the user’s last update become more difficult, because the code running on one device doesn’t know what updates have happened on the other device. This metadata will need to be centralized.
- If your replicas are distributed across different datacenters, there is no guarantee that connections from different devices will be routed to the same datacenter. If your approach requires reading from the leader, you may first need to route requests from all of a user’s devices to the same datacenter.

### Monotonic Reads
This anomaly can occur when reading from asynchronous followers, its when it’s possible for a user to see things _moving backward in time_.

For example:
 1. User 2345 makes the same query twice, first to a follower with little lag, then to a follower with greater lag.
 2. The first query returns a comment that was recently added by user 1234
 3. The second query doesn’t return anything because the lagging follower has not yet picked up that write, observing the system at an earlier point in time than the first query.

_Monotonic reads is a guarantee that this kind of anomaly does not happen_. It’s a lesser guarantee than strong consistency, but a stronger guarantee than eventual consistency. Monotonic reads means that if one user makes several reads in sequence, they will not see time go backwards.

One way of achieving monotonic reads is to make sure that each user always makes their reads from the same replica, with the replica being chosen based on some arbitrary value, like a hash of the user ID, rather than randomly, though if that replica fails, the user’s queries should be rerouted to another replica.

### Consistent Prefix Reads
This guarantee says that if a sequence of writes happens in a certain order, then anyone reading those writes will see them appear in the same order.

This is a particular problem in [[sharding|partitioned databases]]. The database always applies writes in the same order, reads always see a consistent prefix, so this anomaly cannot happen. However, in many distributed databases, different partitions operate independently, so there is no global ordering of writes: when a user reads from the database, they may see some parts of the database in an older state and some in a newer state.

One solution is to make sure that any writes that are causally related to each other are written to the same partition—but in some applications that cannot be done efficiently. There are also [[causality-tracking|algorithms]] that explicitly keep track of causal dependencies.

## Solutions
There are ways in which an application can provide a stronger guarantee than the underlying database, for example, by performing certain kinds of reads on the leader. However, dealing with these issues in application code is complex and easy to get wrong.

It would be better if application developers didn’t have to worry about subtle replication issues and could just trust their databases to “do the right thing.” This is why [[transactions]] exist: they are a way for a database to provide stronger guarantees so that the application can be simpler.

Single-node transactions have existed for a long time. However, in the move to distributed (replicated and partitioned) databases, many systems have abandoned them, claiming that transactions are too expensive in terms of performance and availability, and asserting that eventual consistency is inevitable in a scalable system. There is some truth in that statement, but it is overly simplistic.
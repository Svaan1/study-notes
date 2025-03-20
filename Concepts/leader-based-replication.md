19.03.2025 19:25
Tags: #concept

---
# Leader Based Replication

Each node that stores a copy of the database is called a replica. Every write to the database needs to be processed by every replica.

One of the replicas is designated the _leader_ When clients want to write to the database, they must send their requests to the leader, which first writes the new data to its local storage.

The other replicas are known as _followers_. Whenever the leader writes new data to its local storage, it also sends the data change to all of its followers as part of a [[replication-log|replication log]] or _change stream_. Each follower takes the log from the leader and updates its local copy of the database accordingly, by applying all writes in the same order as they were processed on the leader.

When a client wants to read from the database, it can query either the leader or any of the followers. However, writes are only accepted on the leader (the followers are read-only from the client’s point of view).
## Synchronous vs Asynchronous
Changes to to all followers in most database systems are applied in less than a second, but there is no strong guarantee of how long it might take, followers might fall behind the leader by several minutes or more.

The advantage of **synchronous** replication is that, by always awaiting for the confirmation of data change success, the follower is guaranteed to have an up-to-date copy of the data that is consistent with the leader. If the leader suddenly fails, we can be sure that the data is still available at the follower, making the fallback process of choosing another leader easier.

The disadvantage is that if the synchronous follower doesn’t respond the write cannot be processed, blocking all writes and waiting until the replica is available again.

For that reason, **it’s impractical for all followers to be synchronous**, in practice, enabling synchronous replication on a database usually means that one of the followers is synchronous and the others are **asynchronous**, sometimes being called **semi-synchronous**.

Leader-based replications are often configured to be completely **asynchronous**. In this case, there is the advantage that the leader can continue processing writes even if all of its followers have fallen behind, but if the leader fails and is not recoverable, any writes that have not yet been replicated to followers are lost. This means that a write is not guaranteed to be durable, even if it has been confirmed to the client.

## Adding New Followers

1. Take a consistent snapshot of the leader’s database at some point in time, if possible, without taking a lock on the entire database. Most databases have this feature, as it is also required for backups. In some cases, third-party tools are needed, such as _innobackupex_ for MySQL.
2. Copy the snapshot to the new follower node.
3. The follower connects to the leader and requests all the data changes that have happened since the snapshot was taken. This requires that the snapshot is associated with an exact position in the leader’s [[replication-log|replication log]]. That position has various names: for example, PostgreSQL calls it the _log sequence number_, and MySQL calls it the _binlog coordinates_.
4. When the follower has processed the backlog of data changes since the snapshot, we say it has _caught up_. It can now continue to process data changes from the leader as they happen.

## Handling Node Outages

How do you achieve high availability with leader-based replication?

### Follower Failure: Catch-up Recovery
If for any reason a follower replica is is temporarily interrupted, the follower can recover quite easily using its data changes log and knowing its last successful transaction, then reconnecting to the leader and requesting all data changes that occurred during the time the follower was disconnected.
### Leader Failure: Failover
One of the follower needs to be promoted to be the new leader, this process being called **fallover**.

Failover can happen manually or automatically, the automatic process usually consists of:

1. Determining the leader has failed.
2. Choosing a new leader, which could be done by an election process, or a new leader could be appointed by a previously elected controller node, usually the best candidate is the replica with the most up-to-date data changes.
3. Re-configuring the system to use the new leader, ensuring that all followers send their writes to the new leader and that the old leader, after it comes back alive, also becomes a follower and recognizes the new leader.

Failover is fraught with things that can go wrong:

- [[replication-lag|Replication lag]]
- [[system-coordination-failure|System coordination failure]]
- [[split-brain-syndrome|Split brain syndrome]]
- [[timeout-tuning-dilemma|Timeout tuning dilemma]]

```ad-bug
There are no easy solution to these problems. For this reason, some operations teams prefer to perform failovers manually, even if the software supports automatic failover.
```


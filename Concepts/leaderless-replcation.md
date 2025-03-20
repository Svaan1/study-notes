20.03.2025 18:55
Tags: #concept

---
# Leaderless Replication

Other [[database-replication|replication]] techniques, such as [[leader-based-replication|single-leader]] and [[multi-leader-replication|multi-leader]] replication are based on the idea that a client sends a write request to the leader and the database system takes care of copying that write to the other replicas.

Some data storage systems take a different approach, abandoning the concept of a leader and allowing any replica to directly accept writes from clients. In some leaderless implementations, the client directly sends its writes to several replicas, while in others, a _coordinator node_ does this on behalf of the client. However, unlike a leader database, that coordinator does not enforce a particular ordering of writes.


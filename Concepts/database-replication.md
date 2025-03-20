19.03.2025 08:46
Tags: #concept

---
# Database Replication

Roughly, replication means keeping the same data across multiple machines connected to a network. Because of the added overhead of maintaining such a system, there needs to be good reasons to apply it, for example, when you need to:

- Keep data geographically close to your users to reduce latency
- Have fault tolerance, so the system as a whole will continue working even if some of its parts have failed
- To be able to scale read queries horizontally, adding more machines to the system

```ad-danger
All of the difficulty in replication lies in handling changes to replicated data, the reading is the easy part.
```

## Types of Replication
- [[leader-based-replication|Leader Based Replication]]
- [[multi-leader-replication|Multi Leader Replication]]
- [[leaderless-replcation|Leaderless Replication]]
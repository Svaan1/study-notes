---
created: 2025-03-19T08:46
type: concept
status: active
area:
  - databases
  - distributed-systems
source:
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
- Leader Based Replication
- Multi Leader Replication
- Leaderless Replication

## Related
- [[leader-based-replication]]
- [[multi-leader-replication]]
- [[leaderless-replication]]

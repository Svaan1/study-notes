26.05.2025 19:50
Tags: #concept

---
# TCC

Concepts that may help
-  DAGs directed acyclic weighted task graphs

Important algorithms
- Heterogeneous Earlist-Finish-Time HEFT
- Critical Path on a Processor CPOP

Good comparisons
- Schedule length ratio and speedup
- Cost - time complexity


Maybe add every execution to an AI, that starts giving nodes tasks arbitrarily, then as every execution gets a log of execution time added to a db, it starts to learn how to better choose nodes

some DAGs usually consider

- **average execution cost** (time complexity) to define task priority
- *data transfer size*, this is usually used to consider the cost of transfering data between processors, as DAGs usually have multiple operation steps involved, and these steps can be done in different processors, checking if the change of the processor is worth the cost of a data transfer is key, uses an average transfer rate between process in the same domain and correlates it with the size of the data
- **Earliest execution start time** and **Earliest execution finish, 


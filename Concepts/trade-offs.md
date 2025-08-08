07.08.2025 19:05
Tags: #concept

---
# Trade-offs

Using a storage system as an example:
- **Performance** can be increased with the **[[sharding]]** of the data centers, distributing the load evenly between instances, but the increased amount of infrastructure and concurrent processes can and most probably will cause a big amount of **faults**.
- **[[fault-tolerance|Fault tolerance]]** in a system can be improved using techniques like **[[replication]]**, but storing the same data across multiple instances can cause **inconsistencies**
- Dealing with **inconsistencies** usually incurs extra steps and increased overhead, lowering the overall **performance** of the system.
 
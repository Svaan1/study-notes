08.01.2025 09:23
Tags: #concept

---
# B-Tree Indexes

As the name states, this type of [[database-indexes|index]] uses [[B-trees]] as the underlying data structure, while also adding additional database specific optimizations.

## Time Complexities

- **Search**: O(log n)
- **Insert**: O(log n)
- **Delete**: O(log n)
- **Space**: O(n)

However, these are only  theoretical complexities, real-world performance depends heavily on:

1. The branching factor (number of keys per node)
2. Whether the data fits in memory or requires disk access
3. How the data is distributed
4. Node split/merge frequency

## Use Cases

**Ideal**:
- Database indexes for sorted *range queries*
- When you need *ordered traversal* of data

**NOT Ideal**:
- Pure equality searches (hash tables are faster)
- Write-heavy workloads with random inserts (due to re balancing overhead)
- Memory-constrained environments (due to overhead per node)
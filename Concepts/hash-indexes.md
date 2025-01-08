04.01.2025 17:11
Tags: #concept

---
# Hash Indexes  

Most commonly used [[database-indexes|index]] in data management. It is created on a column that contains unique values, such as a primary key or email address.

Rarely used over [[b-tree-indexes|b-trees]].

- Only supports exact match queries
- No ordering preserved (can't do range scans)
- Very fast point lookups
- Collisions must be handled (usually with chaining or open addressing)
- Generally needs to fit in memory for best performance

## Time Complexities

- Search (equality): O(1) average case
- Insert: O(1) average case
- Delete: O(1) average case
- Space: O(n)

## Use Cases

Ideal:
- Exact equality searches only
- When range queries aren't needed
- Join operations on equality conditions

Not Ideal:
- Range queries
- Ordered data retrieval
- Pattern matching (LIKE queries)
- Prefix searches
- When data ordering matters

Challenges:
- Collision resolution strategy
- Load factor management
- Resizing/rehashing overhead
- Memory locality not as good as B-trees
- Non-uniform data distribution can lead to clustering
## Considerations

The only case where it would make sense considering them is when the value being indexed is quite large. Values longer than about 2692 bytes will fail altogether when inserted into b-tree, while long values which are shorter than that will succeed but generate quite large indexes which might be less cache/IO friendly.

In PostgreSQL, b-tree indexes have a hard limit on the size of index entries at around 1/3 of the block size. So if even 0.00001% of your table rows might have values longer than the limit, you have a problem. Hash indexes avoid this limitation.

Good when an dealing with the indexing of a quite large field, around 24+ bytes on average (around that length sizes of indexes breaks even. assuming we don't have a lot of duplicate values where `btree index deduplication` optimization kicks in or break even point will be higher)

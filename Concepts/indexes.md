04.01.2025 17:11
Tags: #concept

---
# Concept

# Indexes  
tags: #concept  

An index is any data structure that improves the performance of a lookup.

There are complex design trade-offs involving lookup performance, index size, and index-update performance,

- Improves the speed of data retrieval operations
- Creates additional writes and storage space per insertion or update

## Indexing Methods
### Non-clustered
Improves data retrieval speed by creating a logical order of data that's separate from the physical order of the data on disk, so it doesn’t alter the order of data from the table its indexing. 

Typically non-primary key columns used in JOIN, WHERE, and ORDER BY clauses.

There can be multiple non-clustered index for each table.
### Clustered
- Alters the data block to match the index, resulting in the row data being stored in order.
## Types  
- Fuzzy Indexes

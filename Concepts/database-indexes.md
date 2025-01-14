04.01.2025 17:11
Tags: #concept

---
# Indexes  

An index is any data structure that improves the performance of a lookup, in this case, specifically to [[databases]].

There are complex design trade-offs involving lookup performance, index size, and index-update performance,

- Improves the speed of data retrieval operations
- Creates additional writes and storage space per insertion or update

## Indexing Methods
### Non-clustered
- Creates a logical order of data that's separate from the physical order of the data on disk, so it doesn’t alter the order of data from the table its indexing. 
- Typically non-primary key columns used in JOIN, WHERE, and ORDER BY clauses.
- There can be multiple non-clustered index for each table.
### Clustered
- Alters the data block to match the index, resulting in the row data being stored in order.
- Only one clustered index can be created on a given database table
- Great when data is accessed sequentially in the same or reverse order of the clustered index or when a range of items is selected.
### Cluster
- The records for the tables sharing the value of a cluster key shall be stored together in the same or nearby data blocks.
- When multiple databases and multiple tables are joined
- Can be keyed with a [[b-tree-indexes|B-Tree]] index or a [[hash-indexes|Hash Tables]].
- The data block where the table record is stored is defined by the value of the cluster key.
## Column Order

The order that the index definition defines the columns in is important.

It is possible to retrieve a set of row identifiers using only the first indexed column. However, it is not possible or efficient to retrieve the set of row identifiers using only the second or greater indexed column.

For example, in a phone book organized by city first, then by last name, and then by first name, in a particular city, one can easily extract the list of all phone numbers. However, it would be very tedious to find all the phone numbers for a particular last name. One would have to look within each city's section for the entries with that last name.

In the phone book example with a [[composite-index.md|Composite Index]] created on the columns (`city, last_name, first_name`), if we search by giving exact values for all the three fields, search time is minimal, but if we provide the values for `city` and `first_name` only, the search uses only the `city` field to retrieve all matched records. Then a sequential lookup checks the matching with `first_name`.

```ad-tldr
To improve the performance, one must ensure that the index is created on the order of search columns.
```
## Types  

Different types of indexes can be created for different purposes and performance benefits. Some good factors to consider are:

1. The types of queries you'll be running (equality, range, text search)
2. The [[database-cardinality|cardinality]] of the columns
3. The read/write ratio of your application
4. Available storage space
5. Maintenance overhead and update frequency

Examples of indexes:
- [[b-tree-indexes|B-Tree]] (most common)
- [[hash-indexes|Hash]] (for exact equality lookups)
- [[bitmap-indexes|Bitmap]] (low-cardinality columns)
- [[full-text-search#Indexing|Full Text Search Indexing]] (for searching text content)
- [[spatial-indexes|Spatial]] (for geographic and geometric data)
- [[partial-indexes|Partial]] (for a subset of rows based on a condition)
- [[covering-indexes|Covering]] (index-only scans)[[]]
- [[sparse-indexes|Sparse]]

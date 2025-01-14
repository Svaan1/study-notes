14.01.2025 14:17
Tags: #concept

---
# Partial Indexes

Partial indexes only index the documents in a collection that meet a specified filter expression. By indexing a subset of the documents in a collection, partial indexes have lower storage requirements and reduced performance costs for index creation and maintenance.

## MongoDB
Partial indexes should be preferred over [[sparse-indexes|sparse indexes]]. Partial indexes provide the following benefits:

- Greater control over which documents are indexed.
- A superset of the functionality offered by sparse indexes.

Sparse indexes select documents to index _solely_ based on the existence of the indexed field, or for compound indexes, the existence of the indexed fields.
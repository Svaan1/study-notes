---
created: 2025-01-14T14:19
type: concept
status: active
area:
  - databases
source:
---
# Sparse Indexes

Sparse indexes, generally used in NoSQL, only contain entries for documents that have the indexed field, even if the index field contains a null value.

The index skips over any document that is missing the indexed field. The index is "sparse" because it does not include all documents of a collection. By contrast, non-sparse indexes contain all documents in a collection, storing null values for those documents that do not contain the indexed field.

```ad-tldr
If the sort key doesn't appear in every table item, or if the index partition key is not present in the item, the index is said to be _sparse_.
```

## Related
- [[partial-indexes|Partial Indexes]]
- [[database-indexes]]

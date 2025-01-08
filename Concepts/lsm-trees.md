04.01.2025 17:11
Tags: #concept

---
# LSM-Trees  
tags: #concept  

Log-structured merge-trees (lsm-trees) are the foundation for [[SSTables]].  

### optimizations  
- **non-existent key lookups**: add [[Bloom Filters]].  
- **compaction strategies**:  
  - **size-tiered**: merge newer, smaller sstables into older ones.  
  - **leveled**: organize data into levels for incremental compaction.  

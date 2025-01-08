04.01.2025 17:11
Tags: #concept

---
# SSTables  
tags: #concept  

Persistent, ordered, immutable map from keys to values (byte strings).  

### key concepts  
- **block compression**: group key-value pairs into compressed blocks for efficiency.  
- **construction**: uses balanced trees (*memtables*) to maintain sorted data.  
- **read flow**: query starts with memtable, moving to the newest sstable on disk.  
- **merging/compaction**: periodically combines files, discards overwritten/deleted data.  

### benefits  
- merging is simple, keys remain sorted.  
- binary search-like retrieval efficiency.  

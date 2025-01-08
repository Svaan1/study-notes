04.01.2025 17:10
Tags: #concept

---
# B-Trees  
tags: #concept  

A key-value structure maintaining sorted keys for efficient queries.  

### mechanics  
- organizes data into fixed-size pages (~4kb).  
- uses references (disk pointers) to construct a tree of pages.  
- branching factor (~500): controls references per page.  

### operations  
- **insertion**: locate page, add key; split if full.  
- **update**: locate page, modify key-value, overwrite disk.  

### reliability  
- **write-ahead logs**: ensure crash recovery.  
- **copy-on-write**: avoids overwrites by writing modified pages elsewhere.  

### optimizations  
- sibling references in leaf nodes.  
- space-saving key abbreviations.  
- variants like fractal trees (reduce disk seeks).  



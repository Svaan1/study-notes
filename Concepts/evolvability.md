03.02.2025 17:03
Tags: #concept

---
# Evolvability

Applications inevitably change over time. Features are added or modified as new products are
launched, user requirements become better understood, or business circumstances change.

```ad-summary
We should aim to build systems that make it easy to adapt to change
```

## Compatibility

Compatibility is a relationship between one process that encodes the data, and another process that decodes it.
### Backward Compatibility

Newer code can read data that was written by older code.

Backward compatibility is normally not hard to achieve: as author of the newer code, you know the format of data written by older code, and so you can explicitly handle it (if necessary by simply keeping the old code to read the old data). 

### Forward Compatibility

Older code can read data that was written by newer code.

 Forward compatibility can be trickier, because it requires older code to ignore additions made by a newer version of the code.
### Schema Evolution
The process of managing and implementing changes to a database or data storage schema over time while maintaining compatibility with existing data and applications.

 Schema evolution ensures these changes are handled systematically to avoid disruptions.
 
Allows the same kind of flexibility as schemaless/schema-on-read JSON databases provide, while also providing better guarantees about your data and better tooling.
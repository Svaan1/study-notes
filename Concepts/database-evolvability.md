c03.02.2025 18:17
Tags: #concept

---
# Database Evolvability

In general, it’s common for several different processes to be accessing a database at the same time. 

Those processes might be several different applications or services, or they may simply be several
instances of the same service. Either way, in an environment where the application is changing, it is likely that some processes accessing the database will be running newer code and some will be running older code—for example because a new version is currently being deployed in a rolling upgrade, so some instances have been updated while others haven’t yet.

This means that a value in the database may be written by a newer version of the code, and
subsequently read by an older version of the code that is still running. Thus, forward
compatibility is also often required for databases.

```ad-danger
However, there is an additional snag. Say you add a field to a record schema, and the newer code writes a value for that new field to the database. Subsequently, an older version of the code (which doesn’t yet know about the new field) reads the record, updates it, and writes it back. In this situation, the desirable behavior is usually for the old code to keep the new field intact, even though it couldn’t be interpreted.

Solving this is not a hard problem; you just need to be aware of it.
```
## Archival Storage

Perhaps you take a snapshot of your database from time to time, say for backup purposes or for
loading into a [[data warehouse]]. In this case, the data dump will typically be encoded using the latest schema, even if the original encoding in the source database contained a mixture of schema versions from different eras. Since you’re copying the data anyway, you might as well encode the copy of the data consistently.

As the data dump is written in one go and is thereafter immutable, formats like [[Avro]] object
container files are a good fit. This is also a good opportunity to encode the data in an analytics-friendly column-oriented format such as [[Parquet]].
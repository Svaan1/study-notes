19.03.2025 19:31
Tags: #concept

---
# Replication Log

Replication logs serve as a chronological record of all changes made to a database, capturing the precise sequence and details of operations that modify data.

## Statement-based
The leader logs every statement (request) that it executes and sends that statement log to all followers, each one parsing and executing that statement as if it had been received from a client.

Although this may sound reasonable, there are various ways in which this approach to replication can break down:

- Any statement that calls a nondeterministic function, such as `NOW()` to get the current date and time or `RAND()` to get a random number, is likely to generate a different value on each replica.
- If statements use an auto-incrementing column, or if they depend on the existing data in the database, they must be executed in exactly the same order on each replica, or else they may have a different effect. This can be limiting when there are multiple concurrently executing transactions.
- Statements that have side effects may result in different side effects occurring on each replica, unless the side effects are absolutely deterministic.

It is possible to work around those issues, however, because there are so many edge cases, other replication methods are generally preferred.

## Write-Ahead Log Shipping
Usually, in storage engines, every write is appended to a log:

- In the case of a log-structured engine (see [[sstables|SSTables]] and [[lsm-trees|LSM-Trees]]), this log is the main place for storage. Log segments are compacted and garbage-collected in the background.
- In the case of a [[b-trees|b-tree]], every modification is first written to a write-ahead log so that the index can be restored to a consistent state after a crash.

We can use the exact same log to build a replica on another node. The main disadvantage is that the log describes the data on a very low level, making replication closely coupled to the storage engine. If the database changes its storage format from one version to another, it is typically not possible to run different versions of the database software on the leader and the softwares.


## Logical (row-based) log replication

Uses different log formats for replication and the storage engine, allowing the replication log to be decoupled from the storage internals.

- For an inserted row, the log contains the new values of all columns.
- For a deleted row, the log contains enough information to uniquely identify the row that was deleted. Typically this would be the primary key, but if there is no primary key on the table, the old values of all columns need to be logged.
- For an updated row, the log contains enough information to uniquely identify the updated row, and the new values of all columns (or at least the new values of all columns that changed).
- A transaction that modifies several rows generate several log records, followed by a record indicating that the transaction was committed.

This method makes the replication be more easily kept backward compatible, allowing replicas to run different versions of the database software, or even different storage engines.

A logical log format is also easier for external applications to parse. This aspect is useful if you want to send the contents of a database to an external system, such as a data warehouse for offline analysis, or for building custom indexes and caches [[18](ch05.html#Sharma2015te_ch5)]. This technique is called [[change-data-capture|change data capture]].

## Trigger-based
A trigger lets you register custom application code that is automatically executed when a data change (write transaction) occurs in a database system. The trigger has the opportunity to log this change into a separate table, from which it can be read by an external process. That external process can then apply any necessary application logic and replicate the data change to another system.

Trigger-based replication typically has greater overheads than other replication methods, and is more prone to bugs and limitations than the database’s built-in replication. However, it can nevertheless be useful due to its flexibility.
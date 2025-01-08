08.01.2025 11:09
Tags: #concept

---
# Bitmap Indexes

Bitmap indexes have traditionally been considered to work well for [[database-cardinality|low cardinality]] columns.

Uses bit arrays (commonly called [[bitmaps]]) and answer queries by performing bitwise logic operations on these bitmaps.

They have a significant space and performance advantage over other structures for query of such data. Their drawback is they are less efficient than the traditional [[b-tree-indexes|B-tree indexes]] for columns whose data is frequently updated: consequently, they are more often employed in read-only systems that are specialized for fast query - e.g., data warehouses, and generally unsuitable for online transaction processing applications.

Bitmap indexes are also useful in [[data-warehousing|data warehousing]] applications for joining a large fact table to smaller dimension tables such as those arranged in a [[star-schema|star schema]]

Some disadvantages:
- Poor for high cardinality columns (like email addresses)
- Expensive to update (need to modify multiple bitmaps)
- Can be slower than B-tree for simple queries
- Additional CPU overhead for bitmap operations

## Operation
- Creates a separate bitmap for each distinct value in the indexed column
- Each bitmap has one bit per row in the table
- Bit is set to 1 if the row has that value, 0 otherwise
- Combines bitmaps using bitwise operations (AND, OR, NOT)

	![[Pasted image 20250108111648.png]]

## Time Complexities
- Search: O(1) for simple queries
- Insert: O(n) where n is number of distinct values
- Delete: O(n) where n is number of distinct values
- Space: Very efficient for low cardinality, poor for high cardinality

## Use Cases

Ideal:
- Low cardinality columns (status, gender, category)
- Data warehouse queries
- Complex combinations of AND/OR conditions
- When space efficiency matters
- Read-heavy analytical workloads
- Star schema dimensional tables
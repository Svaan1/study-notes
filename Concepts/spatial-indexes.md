14.01.2025 13:31
Tags: #concept

---
# Spatial Indexes

A **spatial index** is used by a spatial database to optimize spatial queries. Database systems use indices to quickly look up values by sorting data values in a linear order; however, this way of indexing data is not optimal for spatial queries in two- or three-dimensional space. Instead, spatial databases use a _spatial_ index designed specifically for multi-dimensional ordering.[](https://en.wikipedia.org/wiki/Spatial_database#cite_note-GISTBOK_indexing-6)

## SQL Server

In SQL Server, spatial indexes are built using B-trees, which means that the indexes must represent the 2-dimensional spatial data in the linear order of B-trees. Therefore, before reading data into a spatial index, SQL Server implements a hierarchical uniform decomposition of space. The index-creation process _decomposes_ the space into a four-level _grid hierarchy_. These levels are referred to as _level 1_ (the top level), _level 2_, _level 3_, and _level 4_.

Each successive level further decomposes the level above it, so each upper-level cell contains a complete grid at the next level. On a given level, all the grids have the same number of cells along both axes (for example, 4x4 or 8x8), and the cells are all one size.
## Postgres

PostGIS and Oracle Spatial share the same “[[r-tree|R-Tree]]” spatial index structure. R-Trees break up data into rectangles, and sub-rectangles, and sub-sub rectangles, etc. It is a self-tuning index structure that automatically handles variable data density, differing amounts of object overlap, and object size.

![[Pasted image 20250114133852.png]]
In the figure above, the number of lines that intersect the yellow star is **one**, the red line. But the bounding boxes of features that intersect the yellow box is **two**, the red and blue ones.

The way the database efficiently answers the question “what lines intersect the yellow star” is to first answer the question “what boxes intersect the yellow box” using the index  and then do an exact calculation of “what lines intersect the yellow star” **only for those features returned by the first test**.

For a large table, this “two pass” system of evaluating the approximate index first, then carrying out an exact test can radically reduce the amount of calculations necessary to answer a query.
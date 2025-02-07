29.01.2025 19:15
Tags: #concept

---
# Composite Indexes

 Composite indexing, also known as multi-column indexing, is a database optimization technique where an index is created on multiple columns of a table. This type of indexing is particularly useful when queries frequently filter or sort data based on multiple columns.

## Concatenated Index
 Combines several fields into one key by appending one column to another (the index definition specifies in which order the fields are concatenated).
 
This is like an old-fashioned paper phone book, which provides an index from (lastname, firstname) to phone number. Due to the sort order, the index can be used to find all the people with a particular last name, or all the people with a particular lastname-firstname combination. However, the index is useless if you want to find all the people with a particular first name.

## Multi-dimensiona Indexes
Multi-dimensional indexes are a more general way of querying several columns at once,

For example, a restaurant-search website may have a database containing the latitude and longitude of each restaurant. When a user is looking at the restaurants on a map, the website needs to search for all the restaurants within the rectangular map area that the user is currently viewing. This requires a two-dimensional range query.

A standard B-tree or LSM-tree index is not able to answer that kind of query efficiently: it can
give you either all the restaurants in a range of latitudes (but at any longitude), or all the restaurants in a range of longitudes (but anywhere between the North and South poles), but not both simultaneously.

One option is to translate a two-dimensional location into a single number using a space-filling
curve, and then to use a regular [[B-tree index]] More commonly, specialized spatial indexes such as [[R-trees]] are used. For example, PostGIS implements [[spatial-indexes|geospatial indexes]] as R-trees using PostgreSQL’s Generalized Search Tree indexing facility.

An interesting idea is that multi-dimensional indexes are not just for geographic locations. For
example, on an ecommerce website you could use a three-dimensional index on the dimensions (red,
green, blue) to search for products in a certain range of colors, or in a database of weather
observations you could have a two-dimensional index on (date, temperature) in order to
efficiently search for all the observations during the year 2013 where the temperature was between
25 and 30℃.
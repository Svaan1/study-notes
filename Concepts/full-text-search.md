08.01.2025 11:21
Tags: #concept

---
# Full Text Search

Refers to a search of all of the documents' contents within the full-text queries’ range(s) that are relevant. This includes topic, phrasing, citation, or additional text attributes.
## Types

### Simple full-text search
Very basic in that users enter keywords or phrases to find documents containing those specific terms.

**Best use**: These searches are often used as quick searches seeking general information.

### Boolean full-text search 
Uses Boolean operators (e.g., AND, OR, NOT) to either combine or exclude specific keywords in the search query. This not only provides more control of the search results but also helps users narrow down broad topics to the specific information they are seeking.

**Best use**: Often used in complex queries using logical relationships between terms, Boolean full-text searches help users save time and enhance query relevance.
### Fuzzy search
Allows the user to find text that is a “likely” match, meaning that misspelled words, typos, etc. in the desired term can be analyzed as matching user parameters.

**Best use**: These searches are helpful when searching through documents that often have non-traditional spellings, typos, or other irregularities.

### Wildcard search
Wildcard searches include non-alphanumeric characters (e.g., `?`, `*`) representing unknown portions of words. This allows the user to search for variations of words (e.g., part, parted, parting) or partial matches (e.g., summertime, summer vacation, summer).

**Best use**: These searches are helpful when users want to account for different forms or correct spelling variations of a word.

### Phrase search
This search seeks an exact phrase where the words of the phrase queried appear within the document in the order specified.

**Best use**: Phrase searches are often used in queries searching for contextually related terms in long documents (e.g., searching for "2024 income tax brackets" within an IRS website).

### Proximity search
Proximity searches identify and retrieve documents containing specific terms within a set number of words, phrases, or paragraphs from each other.

**Best use**: Proximity searches are useful in narrowing down results when searching long documents on a broad topic. For example, a treatise on marine conservation may include information on all types of marine environments (e.g., deep sea, estuaries, mangroves) but by using a proximity search index when looking for mangrove conservation information, most relevant mangrove information will be retrieved from the document.

### Range search
Range searches look for terms within a numerical or alphabetical range specified by the user.

**Best use**: Range searches are helpful when ranges such as dates, currency values, or alphanumeric medical coding are of interest to a user.

### Faceted search
This type of search helps refine results using predefined categories and specific attributes (e.g., facets) of the topic.

**Best use**: These searches are used every day in e-commerce. The descriptors or attributes — such as medium, blue, and dress shirt — are all facets of the clothing desired by the user.

## Indexing

A full-text search [[database-indexes|index]] is a specialized data structure that enables the fast, efficient searching of large volumes of textual data.

To create a full-text search index, each text field of a dataset is analyzed.

1. Diacritics (marks placed above or below letters, such as é, à, and ç in French) are removed. 
2. Based on the the language the text is written, the algorithms remove filler words and only keep the stem of the terms. This way, “to eat” and “eating” are classified as the same root word: “eat."
3. All text is converted to either all uppercase or lowercase text. Additional steps may also be included depending upon the specific analyzer that is being used to develop the full-text index.
4. The index is created, storing references to where each term (e.g., word, phrase) can be found within the document where it resides.

Once the full-text index is created, it allows for fast lookup and retrieval of documents relevant to a user's search query. Instead of scanning through all the content of every document or all web pages, the search engine can quickly identify the documents that contain the specified terms by consulting the index.

In addition to enhanced query speed, additional optimizations to enhance index speed and storage efficiency are applied. Data caching, data compression, and other data structure optimizations are often employed to create leading-class full-text search systems.

### Index Types
There are various types of full-text indexes to choose from. Search requirements, data type and volume, and query complexity are key points of consideration for the user when selecting the full-text index method.

Two common full-text indexes include [[inverted-indexes|Inverted indexes]] and [[b-tree-indexes|B-tree indexes]].

- **Inverted index**: Inverted indexes are the most commonly used. These indexes store the mapping of terms to the documents in which they're contained. They enable rapid lookups during searches and optimize the search process.

- **B-trees and B+ trees**: B-trees and B+ trees are often used when full-text search is integrated into a relational database. Specifically, they are often used for range queries.
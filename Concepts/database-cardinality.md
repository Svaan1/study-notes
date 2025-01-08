08.01.2025 09:04
Tags: #concept

---
# Database Cardinality

Cardinality refers to the number of unique values in a column relative to the total number of rows in a [[databases|database]].

## Categorization

High Cardinality:
- Many unique values relative to total rows
- Examples: email addresses, usernames, phone numbers
- A `user_id` column where almost every value is unique
- If you have 1 million rows and 900,000 unique values, that's high cardinality

Medium Cardinality:
- A moderate number of unique values
- Examples: city names, age groups, product categories
- If you have 1 million rows and 1,000 unique values, that's medium cardinality

Low Cardinality:
- Few unique values that repeat often
- Examples: status (active/inactive), gender, country codes
- A `subscription_type` column with only values like "free", "basic", "premium"
- If you have 1 million rows but only 5 possible values, that's low cardinality

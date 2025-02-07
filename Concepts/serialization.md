03.02.2025 17:31
Tags: #concept

---
# Serialization

When you want to write data to a file or send it over the network, you have to encode it as some
kind of self-contained sequence of bytes (for example, a JSON document)

The translation from the in-memory representation of this data to a byte sequence is called encoding (also known as serialization or marshalling), and the reverse is called decoding (parsing, deserialization,
unmarshalling).

## Binary Encodings
Although textual data formats such as JSON, XML, and CSV are widespread, binary encodings based on schemas are also a viable option. They have a number of nice properties:

- They can be much more compact than the various “binary JSON” variants, since they can omit field
names from the encoded data.

- The schema is a valuable form of documentation, and because the schema is required for decoding,
you can be sure that it is up to date (whereas manually maintained documentation may easily
diverge from reality).

- Keeping a database of schemas allows you to check forward and backward compatibility of schema
changes, before anything is deployed.

- For users of statically typed programming languages, the ability to generate code from the schema
is useful, since it enables type checking at compile time.
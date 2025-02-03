03.02.2025 18:17
Tags: #concept

---
# Service Evolvability

[[RPC]] clients and servers, for example, can be changed and deployed independently. Compared to data flowing through databases, we can make a simplifying assumption in the case of dataflow through services:

it is reasonable to assume that all the servers will be updated first, and all the clients second, thus, you only need backward compatibility on requests, and forward compatibility on responses.

The backward and forward compatibility properties of an RPC scheme are inherited from whatever
encoding it uses:
- [[Thrift]], [[gRPC]] (Protocol Buffers), and [[Avro]] RPC can be evolved according to the compatibility rules
of the respective encoding format.

- In [[SOAP]], requests and responses are specified with XML schemas. These can be evolved, but there
are some subtle pitfalls

- RESTful APIs most commonly use JSON (without a formally specified schema) for responses, and
JSON or URI-encoded/form-encoded request parameters for requests. Adding optional request
parameters and adding new fields to response objects are usually considered changes that maintain
compatibility.

## Versioning
There is no agreement on how API versioning should work. For RESTful APIs, common approaches are to use a version number in the URL or in the HTTP Accept header.

For services that use API keys to identify a particular client, another option is to store a client’s requested API version on the server and to allow this version selection to be updated through a separate administrative interface.
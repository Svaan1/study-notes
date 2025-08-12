08.08.2025 18:13
Tags: #concept

---
# MapReduce

Aims to make execution of demanding tasks easier by hiding the complexities of handling[[ parallelization]], such as:

- __Inter-machine communication__
- __Partitioning of the input data__: reduces the I/O bottleneck by distributing the input data into thousands of machines, often addressing tasks to machines which its input is present in.
- __Handling failures__: making sure that no task or progress is lost in the eventual failure of one of the machines.

## Programming Model

### Mappings

Receives an input pair and emits intermediate key-value pairs, which are then grouped into values from the same keys and sent to the **reducers**.

pseudo-code:
```python
def map(key: str, value: str):
	# key: document name
	# value: document contents
	for word in value:
		EmitIntermediate(word, "1");
```

### Reduce

Receives an intermediate key and all its associated values from the previous **mappings**, then applies the reducer function via an iterator, so it doesn’t load all the value set at once.

pseudo-code
```python
def reduce(key: str, values: list):
	# key: a word
	# values: a list of counts
	int result = 0;
	for v in values:
		result += int(v); # all values are passed to the functions as strings
		Emit(AsString(result))
```

## Implementation


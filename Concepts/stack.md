10.01.2025 09:10
Tags: #concept

---
# Stack

A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle. Think of it like a stack of plates - you can only add or remove plates from the top.

## Operations

- Push: Add an element to the top
- Pop: Remove the top element
- Peek/Top: View the top element without removing it
- IsEmpty: Check if stack is empty

## When to Use

- When you need to track the most recent element or state
- When you need to process things in reverse order
- When you need to maintain a history of operations
- For backtracking problems
- Matching pairs (like parentheses)

## Structure
```python
def solve_stack_problem(input):
    stack = []  # Initialize empty stack
    
    for element in input:
        # Common pattern 1: Push if condition met
        if some_condition:
            stack.append(element)
        
        # Common pattern 2: Pop and process when needed
        elif stack and some_other_condition:
            top_element = stack.pop()
            # Process top_element
        
        # Common pattern 3: Peek at top without removing
        elif stack and need_to_check_top:
            if stack[-1] == something:
                # Do something
		
    # Common pattern 4: Process remaining elements
    while stack:
        # Process remaining elements
```

## Examples
### Daily Temperatures
```python
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
	result = [0] * len(temperatures)
	stack = []
		
	for i, current in enumerate(temperatures):
		while stack and stack[-1][1] < current:
			top_index, top_value = stack.pop()
			result[top_index] = i - top_index
			stack.append((i,current))
	return result
```

### Car Fleet
```python
def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
	pairs = [(p,s) for p, s in zip(position, speed)]
	pairs.sort(reverse=True)

	stack = []

	for i in range(len(pairs)):
		current_car = (target - pairs[i][0]) / pairs[i][1]
		
		if stack and current_car <= stack[-1]:
			continue
		stack.append(current_car)
	return len(stack)
```
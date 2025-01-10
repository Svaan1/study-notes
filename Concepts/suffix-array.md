10.01.2025 08:55
Tags: #concept

---
# Suffix Array

## Examples

### Trapping Rain Water
```python
class Solution:

def trap(self, height: List[int]) -> int:
	height_size = len(height)
	
	result = 0
	
	left_wall = [0] * height_size
	right_wall = [0] * height_size
	
	left_wall[0] = height[0]
	for i in range(1, height_size):
		left_wall[i] = max(left_wall[i - 1], height[i])
	
	right_wall[-1] = height[-1]
	for i in range(height_size - 2, -1, -1):
		right_wall[i] = max(right_wall[i + 1], height[i])
	
	for i in range(height_size):
		result += min(right_wall[i], left_wall[i]) - height[i]
	
	return result
```


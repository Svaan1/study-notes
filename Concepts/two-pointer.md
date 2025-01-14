09.01.2025 10:29
Tags: #concept

---
# Two Pointer

- GREAT for ordered lists

## Examples
### Skeleton
```python
def solution(numbers: list[int]):
	left_index = 0
	right_index = len(numbers) - 1

	while left_index < right_index:
		if something:
			left_index += 1
		elif something_else:
			right_index -= 1
		else:
			left_index += 1
			right_index -= 1
	
```

### Valid Palindrome
```python
def isPalindrome(self, s: str) -> bool:
	# Starting indexes, one at the the start and one at the end of the string
	left_index = 0
	right_index = len(s) - 1
	
	left_letter = None
	right_letter = None

	# While the right index is still at the right of the left index
	while left_index < right_index:
		left_letter = s[left_index]
		right_letter = s[right_index]
		
		# If non-letter, increase the index and re-start the loop
		if not left_letter.isalnum():
			left_index += 1
			continue
		
		if not right_letter.isalnum():
			right_index -= 1
			continue
		
		# Iterate at both ends everytime, 
		left_index += 1
		right_index -= 1
		
		if left_letter.lower() != right_letter.lower():
		
		return False
  
	return True
```

### Two Sum II
```python
def twoSum(self, numbers: List[int], target: int) -> List[int]:
	left_index = 0
	right_index = len(numbers) - 1
	
	left_number = numbers[left_index]
	right_number = numbers[right_index]
	
	while left_index < right_index:
		current_value = left_number + right_number
		
		if current_value == target:
			return [left_index + 1, right_index + 1]
		
		if current_value > target:
			right_index -= 1
			right_number = numbers[right_index]
			continue
		
		if current_value < target:
			left_index += 1
			left_number = numbers[left_index]
			continue
	
	return []
```

### 3 Sum
```python
def threeSum(self, nums: list[int]) -> list[list[int]]:
	
	nums = sorted(nums)
	result = []
	
	for index in range(len(nums)):
		if index > 0 and nums[index] == nums[index - 1]:
			continue
		
		target = -nums[index]
		left_index = index + 1
		right_index = len(nums) - 1
		
		while left_index < right_index:
			current = nums[left_index] + nums[right_index]
			
			if current == target:
				result.append([nums[index], nums[left_index], nums[right_index]])
				
				while left_index < right_index and nums[left_index] == nums[left_index + 1]:
					left_index += 1
				
				while left_index < right_index and nums[right_index] == nums[right_index - 1]:
					right_index -= 1
				
				left_index += 1
				right_index -= 1
				
			elif current > target:
				right_index -= 1
				
			else:
				left_index += 1
		
	return result
```
### Trapping Rain Water
```python
def trap(self, height: List[int]) -> int:
	left_index = 0
	right_index = len(height) - 1
	
	result = 0
	
	left_max = height[left_index]
	right_max = height[right_index]
	
	# We iterate in a way, that we calculate always knowing the opposite wall is big
	# enough to fit the contents of the current wall
	while left_index < right_index:
		# If the left wall is the lowest, we can go to the next left index and
		# Calculate as if a big enough wall is present on the other side
		# So we just ignore it and calculate between the biggest leftmost wall
		# and the current one
		if left_max < right_max:
			left_index += 1
			left_max = max(left_max, height[left_index])
			result += left_max - height[left_index]
		else:
			right_index -= 1
			right_max = max(right_max, height[right_index])
			result += right_max - height[right_index]
	
	return result
```
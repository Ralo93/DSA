
# Problem-Solving Strategy for Coding Interviews
  
## 1. Clarify Requirements

- Ask clarifying questions
- Understand input/output specifications
- Confirm and handle edge cases
  

## 2. Example Walkthrough

- Create representative sample input
- Manually solve problem step-by-step
- Identify underlying patterns and algorithms

## 3. Initial Solution

- Develop initial approach (may be brute force)
- Demonstrate basic problem understanding
- Discuss initial time/space complexity

## 4. Optimization Techniques

- Reduce time complexity
- Minimize space usage
- Explore alternative data structures
- Identify potential algorithmic improvements

## 5. Code Implementation

- Write clean, modular code
- Use meaningful variable names
- Implement robust error handling
- Follow language best practices

## 6. Complexity Analysis

- Calculate Big O time complexity
- Analyze space requirements
- Explain algorithmic trade-offs

# Key Skills

- Clear communication
- Strong algorithmic thinking
- Efficient coding techniques
- Systematic problem decomposition

# Core Algorithms:
![algomaster](https://github.com/user-attachments/assets/841a3644-2991-49fa-b1c3-620264ebe45a)

# Patterns

## - Prefix Sum Pattern

Given an array like 

```python
array = [1, 2, 3, 4, 5]
```
The prefix sum array will look like:

```python
array = [1, 3, 6, 10, 15]
```
Now you can query the SUM of a subarray like: SUM[i, j] = P[j] - P[i-1]


- Two Pointer
- Binary Search 
- DFS
- BFS
## - Sliding Window

This is basically also a two pointer problem, where you store the intermediate results, BUT you dont want to calculate the full result every time.
Maintain the pointers one by one, so e.g. take the new element which entered the window and subtract the element which got out of the window. Keep a rolling sum from the previous element.
  
 -> 2 calculations instead of calculating the whole sum. For large numbers, this is still 2 calculations instead of thousands!
 So the new sum can be calculated in constant time instead of k.

 So in most cases it is something like this:

 ```python
left = 0
current_sum = 0
minimum_length = math.inf

for right in range(len(nums)):
  curr_sum += nums[right]

  while curr_sum >= target:
    minimum_length = min(minimum_lenght, right-left+1)
    current_sum -= nums[left]
    left += 1

return minimum_length if minimum_length != math.inf else 0

```
 
  
Ask WHY does some algorithm actually work?

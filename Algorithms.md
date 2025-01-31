![image](https://github.com/user-attachments/assets/2752dabd-1085-49fa-bde1-fd972138e637)


## How to know if I should take a for or a while loop:

### FOR LOOP

- Knowing the number of iterations beforehand. E.g. sliding window.
- Iterating over a sequence
- Iterating in order
- the loop should not be interrupted

### WHILE LOOP

- You dont k now how many iterations you need
- The loop should continue until a condition is met
- Complex iteration logic
- Need for modifying the loop control variable within the loop

Example:

```python
def birthday(s, d, m):

    # sum of elements should be d, length of elements should be m
    # return should be number of sub-arrays which meet the conditions
    
    if m > len(s):
        return 0
        
    sub_array_counter = 0
    curr_sum = sum(s[:m])
    
    if curr_sum == d:
        sub_array_counter += 1
        
    for i in range(len(s) - m): # we dont go until len(s) - m  + 1 because we will add the last element in the foor loop instead.
        
        curr_sum = curr_sum - s[i] + s[i+m]
        
        if curr_sum == d:
            sub_array_counter += 1
            
    return sub_array_counter
```

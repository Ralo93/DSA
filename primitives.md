## Primitives in Python

### INT

- Represented in memory as a PyLongObject
- Small integers might be cached (interned) for performance
- In Python ints are of dynamic size


### STRINGS (immutable)

- Represented as UTF-8 or more compact: ASCII (usually)
- Strings also might be interned
- Chars are strings of the length 1
- Memory efficient

## LISTS

- Mutable
- Any data types together
- NOT memory efficient
- many operations

## ARRAYS

- Mutable
- ONE data type
- memory efficient
- e.g. numpy array (which also supports multithreading and is implemented in C)

## STACKS & QUEUES

- Stacks are last-in, first-out (LIFO)
- Queues are first-in, first-out (FIFO)

- Stacks can easily be implemented in python using lists
```python
stack = []
stack.apend(1) # the Push method
stack.append(2)
stack.pop() # The pop method
```
Both Operations are in O(1) BUT stack.pop(0) has O(N). Use collections.deque here becaus deque.popleft() has O(1)


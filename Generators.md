# Generators

Generators are great for large dataset processing or streaming, as they return one item (which can be a batch of a dataset or a line of a read in file) at a time, making it possible to not store the entire dataset in memory.

A generator expression looks like this: (there is no tuple comprehension in python):

```python

squares = (x**2 for x in range(1000))
```


# Python Implementations you should know


## Typehints

-> List should return a List

## Lambda Functions

Lets do an example:

```python
arr = [1, 2, 3, 4, 5]

# Square all even numbers
new_array = list(map(lambda x: x**2, list(filter(lambda x: x % 2 == 0, arr))))
```

lambda Functions are in this form: lambda {arguments} : {operation}

## Map, Reduce and Filter

Map and Filter are already part of python itself, only reduce needs to be imported from functools.reduce().
All take a function and an iterable as an argument.

The trick is to get the function right.

For Map, you need a function which maps one element to itself. E.g. 
```python
lambda x: x**2
```
For Filter, you need a function which checks an element against a condition and returns either True or False. E.g.
```python
lambda x: x % == 0
```
And for Reduce, you need a function which computes one element with its next element from the iterable. This is the only function of those three, which takes two arguments. E.g.
```python
lambda x, y: x + y
```



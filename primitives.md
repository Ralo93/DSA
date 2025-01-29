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

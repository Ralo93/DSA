# Basic generator function
def simple_generator():
    yield 1
    yield 2
    yield 3

# Generator expression
squares = (x**2 for x in range(1000))


gen = simple_generator()

for i in squares:
    print(i)
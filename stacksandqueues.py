
class Stack:
    def __init__(self):
        self._data = []

    def push(self, data):
        self._data.append(data)

    def pop(self):
        return self._data.pop()
    
    def peek(self):
        return self._data[len(self._data)-1]
    

from collections import deque

#faster in adding elements at the end

d = deque("hello") # takes an iterable as an argument

d.append("4")
d.append("5")
d.appendleft("5")
d.popleft()
d.clear()
print(d)

d.extend([1, 2, 3])
d.extendleft([5, 6, 7])

d.rotate(-1) # positives will rotate to the right, negatives will rotate to the left

p = deque("hello", maxlen=5) #the attribute is not writable anymore after initialization!

p.append(1) # so there is a last element added, but the first one gets out
p.extend([1, 2, 3])
print(p)


#stack = Stack()
#stack.push(1)

#print(stack.peek())
#element = stack.pop()
#print(element)
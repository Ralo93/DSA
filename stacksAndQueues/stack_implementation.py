

class Stack:

    def __init__(self, list):

        self.values = list
        print(self.values)

    def pop(self):

        item = self.values.pop()
        return item
    

    def push(self, value):

        self.values.append(value)

    def peek(self):

        print(self.values[-1])
        return self.values[-1]



list = [1, 2, 3, 4, 5]

stack = Stack(list)

print(stack)

stack.pop()
stack.pop()
stack.pop()

stack.push(10)
stack.push(100)
stack.push(1000)

stack.pop()

stack.peek()


def test_stack_push(stack, value):

    stack.push(value)

    assert stack.peek() == value
    print("Assertion cleared!")



test_stack_push(stack, 100)

test_stack_push(stack, 1100)

test_stack_push(stack, 1003)

test_stack_push(stack, 0)

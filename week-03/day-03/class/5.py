# Create a `Stack` class that stores elements
# It should have a `size` method that returns number of elements it has
# It should have a `push` method that adds an element to the stack
# It should have a `pop` method that returns the last element form the stack and also deletes it from it

# please don`t use the built in methods

class Stack(object):
    def __init__(self):
        self.nums = []

    def size(self):
        i = 0
        for elements in self.nums:
            i += 1
        return i

    def push(self, num):
        self.nums += [num]

    def pop(self):
        last_item = self.nums[-1]
        self.nums = self.nums[0:-1]
        return last_item

stack1 = Stack()

stack1.push(2)
stack1.push(3)
stack1.push(3)
stack1.push(3)
print(stack1.pop())
print(stack1.pop())

print(stack1.nums)
# print(stack1.size())

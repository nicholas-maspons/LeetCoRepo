# 232. Implement Queue using Stacks

class MyQueue(object):

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x):
        self.stack_in.append(x)
        
    def pop(self):
        if self.empty():
            raise Exception("Queue is empty")

        if len(self.stack_out) == 0:
            while len(self.stack_in) > 0:
                self.stack_out.append(self.stack_in.pop())
        
        return self.stack_out.pop()

    def peek(self):
        if self.empty():
            raise Exception("Queue is empty")

        if len(self.stack_out) > 0:
            return self.stack_out[-1]

        return self.stack_in[0]

    def empty(self):
        return len(self.stack_in) == 0 and len(self.stack_out) == 0


obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.pop())

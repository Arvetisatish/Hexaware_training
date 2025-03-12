class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print('Stack is empty')
            return None
        # if len(self.stack) < 1:
        #     return None
        # else:
        #     return self.stack.pop()

    def display(self):
        print(self.stack)

    def is_empty(self):
        return len(self.stack) == 0


Stack1 = Stack()
Stack1.push(1)
Stack1.push(True)
Stack1.push(3)

Stack1.display()
Stack1.pop()
Stack1.display()
Stack1.pop()
Stack1.display()
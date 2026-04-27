class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(item, "added to stack")

    def pop(self):
        if not self.items:
            print("Stack is empty")
        else:
            removed = self.items.pop()
            print(removed, "removed from stack")

    def display(self):
        print("Stack elements:", self.items)


s = Stack()

s.push("Apple")
s.push("Banana")
s.push("Mango")

s.display()

s.pop()
s.pop()
s.pop()
s.pop()
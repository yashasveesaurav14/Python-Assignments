from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)
        print(item, "inserted into queue")

    def dequeue(self):
        if not self.queue:
            print("Queue is empty")
        else:
            removed = self.queue.popleft()
            print(removed, "deleted from queue")

    def display(self):
        print("Queue elements:", list(self.queue))


q = Queue()

q.enqueue(101)
q.enqueue(102)
q.enqueue(103)
q.display()

q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
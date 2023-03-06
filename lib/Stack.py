class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = []
        self.limit = limit
        for item in items:
            self.items.append(item)

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        return None if self.full() else self.items.append(item)

    def pop(self):
        return None if len(self.items) <= 0 else self.items.pop()

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        for i in range (0, len(self.items)):
            if target == self.items[i]:
                return len(self.items) - i-1
        return -1
class Queue:
    def __init__(self,n):
        self.queue = [None]*n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def peek(self):
        if self.size != 0:
            x = self.queue[self.head]
            return x
        else:
            return "None"

    def is_empty(self):
        return self.size == 0

    def push(self, val):
        if self.size != self.max_n:
            self.queue[self.tail] = val
            self.tail = (self.tail+1)%self.max_n
            self.size += 1
        else:
            return "error"

    def pop(self):
        if self.is_empty():
            return "None"
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head+1) % self.max_n
        self.size -= 1
        return x


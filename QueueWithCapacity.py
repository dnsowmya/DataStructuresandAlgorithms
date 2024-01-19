class Queue:
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.Top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isFull(self):
        if self.Top + 1 == self.start:
            return True
        elif self.start == 0 and self.Top + 1 == self.maxSize:
            return True
        else:
            return False

    def isEmpty(self):
        if self.Top == -1:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.isFull():
            return "Queue is Full"
        else:
            if self.Top + 1 == self.maxSize:
                self.Top = 0
            else:
                self.Top += 1
                if self.start == -1:
                    self.start = 0
                self.items[self.Top] = value
                return "Element Inserted"

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.Top:
                self.start = -1
                self.Top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement

    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.items[self.start]

    def delete(self):
        self.items = self.maxSize * [None]
        self.Top = -1
        self.start = -1



customQueue = Queue(3)
print(customQueue.isFull())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
print(customQueue.dequeue())
print(customQueue)



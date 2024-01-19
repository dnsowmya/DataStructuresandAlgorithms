class PlateStack():
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def __str__(self):
        return self.stacks

    def push(self, item):

        if len(self.stacks) > 0 and len(self.stacks[-1]) < self.capacity:
            print(f"Step1: {self.stacks[-1]}")
            self.stacks[-1].append(item)
            print(f"Step1: {self.stacks[0]}")
            print(f"Step1: {self.stacks[-1]}")
        else:
            print(f"Step2: {self.stacks}")
            self.stacks.append([item])

    def pop(self):
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop()

    def pop_at(self, stackNumber):
        if len(self.stacks[stackNumber]) > 0:
            return self.stacks[stackNumber].pop()
        else:
            return None

customStack = PlateStack(2)
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack.pop())
customStack.push(4)
customStack.push(5)
print(customStack.pop_at(0))

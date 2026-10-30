class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if len(self.min) < 1:
            self.min.append(value)
        else:
            self.min.append(value if value < self.min[-1] else self.min[-1])

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.min = self.min[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
        

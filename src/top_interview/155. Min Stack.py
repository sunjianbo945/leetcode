class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []
        self.min_val = float('inf')

    def push(self, x: int) -> None:
        self.stack.append(x)
        if x < self.min_val:
            self.min_val = x

        self.min_stack.append(self.min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_val = self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == '__main__':
    a=["push", "push", "getMin", "getMin", "push", "getMin", "getMin", "top", "getMin", "pop", "push", "push",
     "getMin", "push", "pop", "top", "getMin", "pop"]
    b = [ [-10], [14], [], [], [-20], [], [], [], [], [], [10], [-7], [], [-7], [], [], [], []]
    s = MinStack()
    for i in range(len(a)):
        if a[i]=='push':
            s.push(b[i][0])
        elif a[i] == 'top':
            print(s.top())
        elif a[i] == 'getMin':
            print(s.getMin())
        else:
            s.pop()
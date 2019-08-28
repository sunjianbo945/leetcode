class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
        self.is_visited = False

# python list can be stack and queue
#   stack use pop()
#   queue use pop(0)

def bfs(node:Node):
    q = []
    # Put item into the queue.
    q.append(node)

    while not len(q):
        # Remove and return an item from the queue
        element = q.pop(0)
        next_layer_elements = element.get_neighbours()
        for ele in next_layer_elements:
            if not ele.is_visited:
                q.append(ele)
                ele.is_visited = True


def dfs(node: Node):
    q = []
    # Put item into the queue.
    q.append(node)

    while not len(q):
        # Remove and return an item from the stack
        element = q.pop()
        next_layer_elements = element.get_neighbours()
        for ele in next_layer_elements:
            if not ele.is_visited:
                q.append(ele)
                ele.is_visited = True


# A simple class stack that only allows pop and push operations
class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)

# And a queue that only has enqueue and dequeue operations
class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)
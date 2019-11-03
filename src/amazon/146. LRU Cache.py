class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.memo = {}
        self.capacity = capacity

    def get(self, key: int) -> int:

        if key not in self.memo:
            return -1
        else:
            node = self.memo[key]
            self.move_to_head(node)
            return node.val

    def move_to_head(self, node):

        node.next.pre = node.pre
        node.pre.next = node.next

        node.pre = self.head
        node.next = self.head.next

        self.head.next = node
        node.next.pre = node

    def put(self, key: int, value: int) -> None:

        if key in self.memo:
            self.memo[key].val = value
            self.get(key)
        else:
            node = Node(key, value)
            self.memo[key] = node

            node.pre = self.head
            node.next = self.head.next

            self.head.next = node
            node.next.pre = node

            if len(self.memo) > self.capacity:
                self.remove(self.tail.pre)

    def remove(self, node):

        node.pre.next = node.next
        node.next.pre = node.pre

        node.pre = None
        node.next = None

        del self.memo[node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
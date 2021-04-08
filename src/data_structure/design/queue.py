# https://leetcode.com/problems/design-circular-queue/
class MyCircularQueue622:

    def __init__(self, k: int):
        self.front = self.end = None
        self.arr = [-1] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False

        if self.front == self.end is None:
            self.front = self.end = 0
            self.arr[self.front] = value
            return True

        self.end += 1
        self.end %= len(self.arr)
        self.arr[self.end] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        if self.front == self.end:
            self.front = self.end = None
            return True

        self.front += 1
        self.front %= len(self.arr)
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.arr[self.front]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.arr[self.end]

    def isEmpty(self) -> bool:
        return self.front == self.end is None

    def isFull(self) -> bool:
        if self.isEmpty(): return False
        return self.front == ((self.end + 1) % len(self.arr))


# https://leetcode.com/problems/design-circular-deque/
class MyCircularDeque641:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.front = self.end = None
        self.arr = [-1] * k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull(): return False

        if self.front == self.end is None:
            self.front = self.end = 0
            self.arr[self.front] = value
            return True

        self.front -= 1
        self.front %= len(self.arr)
        self.arr[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull(): return False

        if self.front == self.end is None:
            self.front = self.end = 0
            self.arr[self.front] = value
            return True

        self.end += 1
        self.end %= len(self.arr)
        self.arr[self.end] = value
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty(): return False

        if self.front == self.end:
            self.front = self.end = None
            return True

        self.front += 1
        self.front %= len(self.arr)
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty(): return False

        if self.front == self.end:
            self.front = self.end = None
            return True

        self.end -= 1
        self.end %= len(self.arr)
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty(): return -1

        return self.arr[self.front]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty(): return -1

        return self.arr[self.end]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.front == self.end is None

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if self.isEmpty(): return False
        return self.front == ((self.end + 1) % len(self.arr))

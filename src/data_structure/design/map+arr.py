from collections import defaultdict
from random import choice


# https://leetcode.com/problems/insert-delete-getrandom-o1/
class RandomizedSet380:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}  # insert and delete O(1)
        self.arr = []  # O(1) for get random

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.dict:
            self.dict[val] = len(self.arr)
            self.arr.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            curr_idx = self.dict[val]
            self.dict[self.arr[-1]] = curr_idx
            self.arr[curr_idx] = self.arr[-1]
            self.arr.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.arr)


# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/
class RandomizedCollection381:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # here need a set instead of list since the after a free insert and delete the order may change
        self.dict = defaultdict(set)  # insert and delete O(1).
        self.arr = []  # O(1) for get random

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.dict[val].add(len(self.arr))
        self.arr.append(val)
        return len(self.dict[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.dict[val]: return False
        last_num = self.arr[-1]
        removed_idx = self.dict[val].pop()
        self.dict[last_num].add(removed_idx)
        self.dict[last_num].discard(len(self.arr) - 1)
        self.arr[removed_idx] = last_num
        self.arr.pop()

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return choice(self.arr)

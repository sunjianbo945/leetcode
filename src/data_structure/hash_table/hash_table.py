import collections
import itertools
from collections import defaultdict, Counter
from random import choice
from typing import List


# https://leetcode.com/problems/valid-anagram/
class Solution242:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(list(s)) == Counter(list(t))


# https://leetcode.com/problems/find-all-anagrams-in-a-string/
class Solution438:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        p_counter = Counter(p)
        s_counter = Counter()
        res = []
        for i in range(m):
            char = s[i]
            s_counter[char] += 1

            if i >= n:
                old = s[i - n]
                s_counter[old] -= 1
                if s_counter[old] == 0:
                    del s_counter[old]

            if p_counter == s_counter:  # O(1) since only 26 chars
                res.append(i - n + 1)

        return res


# https://leetcode.com/problems/group-anagrams/
class Solution49:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def serialize(s):
            arr = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                arr[idx] += 1

            return ','.join(map(str, arr))

        code_anagrams = defaultdict(list)

        for s in strs:
            code = serialize(s)
            code_anagrams[code].append(s)

        return code_anagrams.values()


# https://leetcode.com/problems/group-shifted-strings/
class Solution249:
    def groupStrings(self, strs: List[str]) -> List[List[str]]:
        def serialize(s):
            arr = [0] * 26
            p = s[0]
            for c in s:
                idx = ord(c) - ord(p)
                arr[idx] += 1

            return ','.join(map(str, arr))

        code_anagrams = defaultdict(list)

        for s in strs:
            code = serialize(s)
            code_anagrams[code].append(s)

        return code_anagrams.values()


# https://leetcode.com/problems/palindrome-permutation/
class Solution266:
    def canPermutePalindrome(self, s: str) -> bool:
        char_count = Counter(list(s))
        count_odd = 0
        for char, count in char_count.items():
            if count % 2 == 1:
                count_odd += 1

        return count_odd <= 1


# https://leetcode.com/problems/maximum-swap/
class Solution670:
    def maximumSwap(self, num: int) -> int:
        A = list(map(int, str(num)))
        num_idx = {x: i for i, x in enumerate(A)}  # duplicate does not matter
        for idx, n in enumerate(A):
            for k in range(9, -1, -1):
                if k <= n: break
                if k > n and k in num_idx and num_idx[k] > idx:
                    A[idx], A[num_idx[k]] = A[num_idx[k]], A[idx]
                    return ''.join(map(str, A))

        return num


# https://leetcode.com/problems/prison-cells-after-n-days/
class Solution957:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        prison_pos = {}
        curr_cells = tuple(cells)
        n = len(cells)
        for i in range(N):

            temp = [1 if curr_cells[i - 1] == curr_cells[i + 1] else 0 for i in range(1, n - 1)]
            curr_cells = tuple([0] + temp + [0])
            if curr_cells in prison_pos:  # 0,1,2,3,4,5=3,6,7,8
                old_pos = prison_pos[curr_cells]
                length = i - old_pos
                return self.prisonAfterNDays(curr_cells, (N - 1 - i) % length)

            prison_pos[curr_cells] = i

        return curr_cells


# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/
class SparseVector1570:
    def __init__(self, nums: List[int]):  # O (n)
        self.idx_num = defaultdict(int)
        for idx, num in enumerate(nums):
            if num:
                self.idx_num[idx] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:  # O(min(l1,l2))
        if len(self.idx_num) < len(vec.idx_num):
            one, another = self.idx_num, vec.idx_num
        else:
            one, another = vec.idx_num, self.idx_num
        res = 0
        for idx, num in one.items():
            res += num * another[idx]

        return res


# https://leetcode.com/problems/sentence-similarity/
class Solution734:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2): return False

        dictionary = defaultdict(set)
        for w1, w2 in similarPairs:
            dictionary[w1].add(w2)
            dictionary[w2].add(w1)

        for w1, w2 in zip(sentence1, sentence2):
            if w1 == w2: continue
            if w2 not in dictionary[w1]:
                return False

        return True


# https://leetcode.com/problems/design-hashmap/
class MyHashMap706:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.space = 1000
        self.hash_table = [Node(-1, -1)] * self.space

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        pos = key % self.space
        head = self.hash_table[pos]
        curr = head

        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next

        curr.next = Node(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        pos = key % self.space
        head = self.hash_table[pos]
        curr = head

        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next

        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        pos = key % self.space
        head = self.hash_table[pos]
        curr = head

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


# https://leetcode.com/problems/subdomain-visit-count/
class Solution811:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        domain_count = Counter()
        for cd in cpdomains:
            count, domain = cd.split(' ')
            parts = domain.split('.')
            for i in range(len(parts)):
                curr = '.'.join(parts[i:])
                domain_count[curr] += int(count)

        return [f'{count} {domain}' for domain, count in domain_count.items()]



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
        self.arr[removed_idx] = last_num

        self.dict[last_num].discard(len(self.arr) - 1)
        self.arr.pop()

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return choice(self.arr)



# https://leetcode.com/problems/swap-for-longest-repeated-character-substring/
class Solution1156:
    def maxRepOpt1(self, text: str) -> int:
        # print([[a,list(b)] for a,b in itertools.groupby(text)])
        A = [[c, len(list(g))] for c, g in itertools.groupby(text)]
        count = collections.Counter(text)

        res = max(min(k + 1, count[c]) for c, k in A)
        # print(res)

        for i in range(1, len(A) - 1):

            if A[i - 1][0] == A[i + 1][0] and A[i][1] == 1:
                res = max(res, min(A[i - 1][1] + A[i + 1][1] + 1, count[A[i + 1][0]]))

        return res

# https://leetcode.com/problems/single-number-iii/
class Solution260:
    def singleNumber(self, nums: int) -> List[int]:
        hashmap = Counter(nums)
        return [x for x in hashmap if hashmap[x] == 1]
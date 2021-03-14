from collections import defaultdict, Counter
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

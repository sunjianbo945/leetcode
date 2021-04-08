from typing import List


# https://leetcode.com/problems/word-search-ii/
class Solution212:
    def createTrie(self, words):
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})

            node['-'] = word

        return trie

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 0(M(4⋅3^{L−1})), where M is the number of cells in the board and L is the maximum length of words.
        # O(N), where N is the total number of letters in the dictionary.
        trie = self.createTrie(words)
        m, n = len(board), len(board[0])
        res = []
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        seen = set()

        def dfs(x, y, trie):
            if x < 0 or y < 0 or x >= m or y >= n or (x, y) in seen or board[x][y] not in trie:
                return

            seen.add((x, y))

            char = board[x][y]
            curr_node = trie[char]
            word_match = curr_node.pop("-", False)
            if word_match:
                res.append(word_match)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                dfs(nx, ny, curr_node)

            seen.remove((x, y))
            if not curr_node:
                trie.pop(char)

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, trie)
        return res


# https://leetcode.com/problems/implement-trie-prefix-tree/
class Trie208:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for c in word:
            if not curr.containsChar(c):
                curr.insert(c)

            curr = curr.getChar(c)

        curr.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for c in word:
            if not curr.containsChar(c):
                return False

            curr = curr.getChar(c)

        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for c in prefix:
            if not curr.containsChar(c):
                return False

            curr = curr.getChar(c)

        return curr.isEnd or curr.node


class TrieNode:
    def __init__(self):
        self.node = {}
        self.isEnd = False

    def containsChar(self, c):
        return c in self.node

    def getChar(self, c):
        return self.node[c]

    def insert(self, c):
        self.node[c] = TrieNode()

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

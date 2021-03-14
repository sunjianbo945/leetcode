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
        # 0(M(4⋅3^{L−1})), where MMM is the number of cells in the board and LLL is the maximum length of words.
        # O(N), where NNN is the total number of letters in the dictionary.
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

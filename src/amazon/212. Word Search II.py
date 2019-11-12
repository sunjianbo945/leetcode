from typing import *

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        for word in words:
            trie.add(word)

        res = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, trie.trie, '', res)

        return res

    def dfs(self, board, i, j, trie, cur, res):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return

        if board[i][j] not in trie:
            return
        else:
            temp = board[i][j]
            if '-' in trie[temp]:
                res.add(cur + temp)

            board[i][j] = '#'
            self.dfs(board, i + 1, j, trie[temp], cur + temp, res)
            self.dfs(board, i - 1, j, trie[temp], cur + temp, res)
            self.dfs(board, i, j + 1, trie[temp], cur + temp, res)
            self.dfs(board, i, j - 1, trie[temp], cur + temp, res)
            board[i][j] = temp


class Trie:
    def __init__(self):
        self.trie = {}

    def add(self, word):
        layer = self.trie

        for w in word:
            if w not in layer:
                layer[w] = {}

            layer = layer[w]

        layer['-'] = True


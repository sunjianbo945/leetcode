from collections import defaultdict
from typing import List


# https://leetcode.com/problems/synonymous-sentences/
class Solution1258:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        graph = defaultdict(set)
        for a, b in synonyms:
            graph[a].add(b)
            graph[b].add(a)

        res = []
        words = text.split(' ')
        n = len(words)

        def dfs(i, curr):
            if i >= n:
                res.append(' '.join(curr))
                return

            word = words[i]
            queue = [word]
            seen = {word}
            while queue:
                curr_word = queue.pop(0)

                curr.append(curr_word)
                dfs(i + 1, curr)
                curr.pop()

                for neighbor in graph[curr_word]:
                    if neighbor in seen: continue

                    seen.add(neighbor)
                    queue.append(neighbor)

        dfs(0, [])
        return sorted(res)


# https://leetcode.com/problems/word-ladder-ii/
class Solution126:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wd = set(wordList)
        wd.add(beginWord)
        if endWord not in wd: return []
        graph = self.bfs(beginWord, endWord, wd)
        seen = set()
        res = []

        def dfs(word, curr):
            if word == endWord:
                res.append(list(curr))
                return

            word_step = graph[word]
            for neighbor in self.getNeighbors(word, seen, graph):
                if graph[neighbor] > graph[word]:
                    curr.append(neighbor)
                    dfs(neighbor, curr)
                    curr.pop()

        dfs(beginWord, [beginWord])
        return res

    def bfs(self, beginWord, endWord, wd):
        queue = [beginWord]
        seen = {beginWord: 0}
        step = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                word = queue.pop(0)

                if word == endWord: return seen

                for neighbor in self.getNeighbors(word, seen, wd):
                    seen[neighbor] = step
                    queue.append(neighbor)

            step += 1

        return seen

    def getNeighbors(self, word, seen, wd):
        n = len(word)
        res = []
        for i in range(n):
            for char in range(26):
                new_word = word[:i] + chr(char + ord('a')) + word[i + 1:]
                if new_word in wd and new_word not in seen:
                    res.append(new_word)
        return res
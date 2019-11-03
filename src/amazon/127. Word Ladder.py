from typing import  *


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        queue = [endWord]

        word_set = set(wordList)
        word_set.add(beginWord)
        visited = {endWord}
        total = 0

        while queue:

            size = len(queue)
            total += 1
            for i in range(size):
                word = queue.pop(0)

                if word == beginWord:
                    return total

                neighbors = self.getAllWords(word, word_set, visited)
                queue.extend(neighbors)

        return 0

    def getAllWords(self, word, word_set, visited):

        res = []

        for i in range(26):

            for j in range(len(word)):

                new_char = chr(ord('a') + i)

                new_word = word[:j] + new_char + word[j + 1:]

                if new_word in word_set and new_word not in visited:
                    res.append(new_word)
                    visited.add(new_word)

        return res

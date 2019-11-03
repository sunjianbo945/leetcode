import heapq


class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alienOrder(self, words):
        # Write your code here
        all_chars = set()

        for word in words:
            for char in list(word):
                all_chars.add(char)

        graph = self.build_graph(words)

        indegree = self.count(graph)

        queue = []

        for char in all_chars:
            if char not in indegree:
                heapq.heappush(queue, char)

        res = ''
        while queue:

            char = heapq.heappop(queue)
            res += char
            for dep in graph.get(char, []):

                indegree[dep] -= 1
                if indegree[dep] == 0:
                    heapq.heappush(queue, dep)

        return res if len(res) == len(all_chars) else ""

    def build_graph(self, words):
        res = {}
        for i in range(len(words) - 1):

            first = words[i]
            second = words[i + 1]
            size = min(len(first), len(second))

            for j in range(size):

                if first[j] != second[j]:
                    if first[j] not in res:
                        res[first[j]] = [second[j]]
                    else:
                        res[first[j]].append(second[j])

                    break
        return res

    def count(self, graph):

        res = {}

        for values in graph.values():
            for val in values:
                if val not in res:
                    res[val] = 1
                else:
                    res[val] += 1

        return res




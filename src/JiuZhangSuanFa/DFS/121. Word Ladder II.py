class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """

    def findLadders(self, start, end, str_dict):
        # write your code here
        str_dict.add(start)
        str_dict.add(end)

        distance_map = self.bfs(start, end, str_dict)
        res = []
        self.dfs(start, end, str_dict, distance_map, [start], res)
        return res

    def dfs(self, start, end, str_dict, distance_map, cur, res):

        if start == end:
            res.append(cur)
            return

        words = self.find_possible_word(start, str_dict, {start})

        min_step = float('inf')

        for word in words:
            dis = distance_map[word]
            min_step = min(dis, min_step)

        for word in words:
            if distance_map[word] == min_step:
                self.dfs(word, end, str_dict, distance_map, cur + [word], res)

    def bfs(self, start, end, str_dict):

        queue = [end]
        visited = {end}
        step = 1
        res = {end: 0}
        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.pop(0)

                words = self.find_possible_word(cur, str_dict, visited)
                for word in words:
                    res[word] = step
                queue.extend(words)

            step += 1

        return res

    def find_possible_word(self, word, str_dict, visited):
        res = []
        for i in range(len(word)):
            for j in range(ord('a'), ord('z') + 1):
                potential = word[:i] + chr(j) + word[i + 1:]
                if potential in str_dict and potential not in visited:
                    res.append(potential)
                    visited.add(potential)
        return res
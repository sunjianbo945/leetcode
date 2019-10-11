class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """

    def ladderLength(self, start, end, str_dict):
        # write your code here
        if not str_dict: return 0

        # if end not in str_dict:return 0
        str_dict.add(start)
        str_dict.add(end)
        queue = [end]
        visited = set()
        visited.add(end)
        total = 1

        while queue:

            size = len(queue)

            for i in range(size):
                node = queue.pop(0)

                # find the start return total
                if node == start:
                    return total
                else:
                    # change string
                    neighbors = self.get_neighbors(node, str_dict, visited)
                    queue.extend(neighbors)

            total += 1

        return 0

    def get_neighbors(self, node, str_dict, visited):
        res = []

        for i in range(len(node)):

            for j in range(ord('a'), ord('z') + 1):

                new_word = node[:i] + chr(j) + node[i + 1:]

                if new_word not in visited and new_word in str_dict:
                    visited.add(new_word)
                    res.append(new_word)

        return res

from collections import defaultdict


class Solution:
    def patterns(self, edges):
        graph = defaultdict(set)
        for idx, edge in enumerate(edges):
            if not edge: continue
            for e in edge:
                graph[idx].add(e)
                graph[e].add(idx)

        min_step = {0: 10}
        articulation = set()

        def dfs(curr, pre, step):
            if curr in min_step: return
            min_step[curr] = step

            for neighbor in graph[curr]:
                if neighbor == pre: continue
                dfs(neighbor, curr, step + 1)

            for neighbor in graph[curr]:
                if neighbor == pre: continue
                min_step[curr] = min(min_step[curr], min_step[neighbor])

            print(curr, pre, min_step[curr], min_step[pre])
            if pre in min_step and min_step[curr] >= min_step[pre] and len(graph[curr]) < 2:
                articulation.add(pre)

        for key, val in graph.items():
            if len(val) > 1 and key not in min_step:
                dfs(key, 0, 0)
        return articulation


print(Solution().patterns([[], [2], [1, 4, 5], [5], [2, 5], [2, 3, 4, 5], [5]]))

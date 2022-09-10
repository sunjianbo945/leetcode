# https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/
from collections import defaultdict
from typing import List


class Solution1761:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        # u_set_v = defaultdict(set)
        # u_connection_count = Counter()
        #
        # for u, v in edges:
        #     u_set_v[min(u, v)].add(max(u, v))  # the same trio only run one time
        #     u_connection_count[u] += 1
        #     u_connection_count[v] += 1
        #
        # ans = inf
        #
        # def find_trio_min(node):
        #     ans_starting_node = inf
        #     for neighbor1 in u_set_v[node]:
        #         for neighbor2 in u_set_v[node]:
        #             # only check 2-> 3 no, need 3->2
        #             if neighbor1 >= neighbor2 or neighbor2 not in u_set_v[neighbor1]:
        #                 continue
        #             ans_starting_node = min(ans_starting_node,
        #                                     u_connection_count[node] +
        #                                     u_connection_count[neighbor1] +
        #                                     u_connection_count[neighbor2] -
        #                                     6)  # - 6 means 3 edge count twice
        #
        #     return ans_starting_node
        #
        # for node in range(1, n + 1):
        #     temp_min = find_trio_min(node)
        #     ans = min(ans, temp_min)
        #
        # return ans if ans < float('inf') else -1

        u_set_v = defaultdict(set)
        for u, v in edges:
            u_set_v[u].add(v)
            u_set_v[v].add(u)

        ans = INF = float('inf')
        degree_node = sorted([[len(u_set_v[k]), k] for k in u_set_v])
        for a, b in edges:
            count_edges_a_b = len(u_set_v[a]) + len(u_set_v[b])
            for count_c, c in degree_node:
                if c in u_set_v[a] and c in u_set_v[b]:
                    ans = min(ans, count_edges_a_b + count_c)
                    break  # must have to shorten run time from 11 s to 0.66 s!!
        return ans - 6 if ans < INF else -1

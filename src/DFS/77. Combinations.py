from typing import *
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.dfs(1, n + 1, k, [], res)
        return res

    def dfs(self, s, e, k, cur, res):
        '''
        s: start position
        e: end position
        k: max number of element
        cur: current list
        res: result list will be return
        '''

        # if current list length = max number of element, put current list to res list
        # boundary condition
        if len(cur) == k:
            # dfs functionality
            res.append(cur)
            return

        # recursion to add other numbers [1,2,3,4     ,5,....n]
        for i in range(s, e):
            self.dfs(i + 1, e, k, cur + [i], res)

            # cur.append(i)
            # self.dfs(i+1,e,k,cur,res)
            # cur.pop()



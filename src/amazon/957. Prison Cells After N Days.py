from typing import *

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:

        pre = [0] * len(cells)
        cur = cells
        memo1={tuple(cells):0}
        memo2={0:cells}
        for i in range(1,N+1):
            pre = cur
            cur = []
            for j in range(1,len(pre)-1):
                val = 1 if pre[j-1] == pre[j+1] else 0
                cur.append(val)

            cur = [0]+cur+[0]
            key = tuple(cur)
            if key not in memo1:
                memo1[key]=i
                memo2[i]=cur
            else:
                recur_count = i-memo1[key]
                place = memo1[key]+ (N-i)%recur_count
                return memo2[place]

        return cur
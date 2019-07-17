# leetcode link
# Difficulty: ***
# https://leetcode.com/problems/binary-watch/
# DFS & BFS

from typing import List

class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        if num == 0:
            return ["0:00"]
        time = ['8h', '4h', '2h', '1h', '32m', '16m', '8m', '4m', '2m', '1m']
        ans = []
        self.dfs_helper(time, num, [], ans)
        return self.transfer(ans)

    def dfs_helper(self, time: List[str], n: int, cur: List[str], result: List[str]):

        if n == 0:
            result.append(cur)
            return

        for i in range(len(time)):
            self.dfs_helper(time[i + 1:], n - 1, cur + [time[i]], result)

    def transfer(self, time: List[List[str]]) -> List[str]:
        ret = []
        for i in range(len(time)):
            h, m = 0, 0
            for j in range(len(time[i])):
                if time[i][j][-1] == 'h':
                    h += int(time[i][j][:-1])
                else:
                    m += int(time[i][j][:-1])
            if h < 12 and m < 60:
                ret.append('{}:{:02d}'.format(h, m))

        return ret


def main():
    print(Solution().readBinaryWatch(1))


if __name__=='__main__':
    main()
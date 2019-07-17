class Solution:
    def climbStairs(self, n: int) -> int:
        map = {}
        map[1] = 1
        map[2] = 2
        self.recur(n, map)

        return map[n]

    def recur(self, n, map) -> int:

        if n in map:
            return map[n]

        if n < 1:
            return 0

        map[n] = self.recur(n - 1, map) + self.recur(n - 2, map)

        return map[n]


def main():
    print(Solution().climbStairs(7))

if __name__=='__main__':
    main()
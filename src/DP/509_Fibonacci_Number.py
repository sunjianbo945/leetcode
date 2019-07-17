class Solution:
    def fib(self, N: int) -> int:

        if N == 0:
            return 0

        if N == 1:
            return 1

        start = 0
        next = 1

        for i in range(N - 1):
            temp = start
            start = next
            next = start + temp

        return next

def main():
    print(Solution().fib(7))


if __name__=='__main__':
    main()
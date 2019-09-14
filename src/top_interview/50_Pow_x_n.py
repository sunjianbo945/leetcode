class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1

        negative = True if n<0 else False

        n = abs(n)

        def recur(x,n):
            if n == 0: return 1
            half = recur(x,n//2)
            if n %2 ==0 : return half*half
            return half*half*x

        ans = recur(x,n)
        return ans if not negative else 1/ans



if __name__ == '__main__':
    print(Solution().myPow(2.0,-2))
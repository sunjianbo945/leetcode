class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        numbers.sort()
        three_closest = float('inf')
        diff = float('inf')
        for i in range(len(numbers)):

            l,r = i+1, len(numbers)-1
            while l<r:
                cur = numbers[i] + numbers[l]+numbers[r]
                if abs(target-cur)<diff:
                    diff = abs(target-cur)
                    three_closest = cur
                if cur>target:
                    r-=1
                else:
                    l+=1

        return three_closest
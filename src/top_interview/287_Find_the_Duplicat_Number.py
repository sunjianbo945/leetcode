import json

class Solution:
    def findDuplicate(self, nums):
        slow = nums[0]
        fast = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        l = nums[0]
        r = slow

        while l != r:
            l = nums[l]
            r = nums[r]

        return l


def stringToIntegerList(input):
    return json.loads(input)


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);

            ret = Solution().findDuplicate(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
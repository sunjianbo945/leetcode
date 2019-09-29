
# def fun1():
#     l=3
#     fun2(l)
#     print(l) # 3
#
# def fun2(a):
#     a=5

# def fun1():
#     l=[]
#     fun2(l)
#     print(l) # [1]
#
# def fun2(a):
#     a.append(1)


# def fun1():
#     l=[3]
#     fun2(l)
#     print(l) # [3, 1]
#
# def fun2(a):
#     a.append(1)

# def fun1():
#     l=[]
#     fun2(l)
#     print(l) # []
#
# def fun2(a):
#     a=[3]

#
# def fun1():
#     l=[3]
#     fun2(l)
#     print(l) # [3]
#
# def fun2(a):
#     a=[7,1]

# def fun():
#     l = [1,2,3]
#     #print(hex(id(l)))
#     fun2(l)
#     print(l)
#
#
# def fun2(m):
#     ret = []
#     for i in m:
#         ret.append((i))
#     m=ret
#     # m = list(m)
#     #print(hex(id(m)))
#     m.append(4)
#     print('m is {}'.format(m))


# def fun():
#     return [i for i in range(5)]
import ctypes
import gc


class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySum(self, nums):
        # write your code here
        if not nums: return []

        cache = {}
        presume = 0

        for i in range(len(nums)):
            presume += nums[i]
            if presume in cache:
                return [cache[presume]+1, i]
            else:
                cache[presume] = i

        return []

if __name__=='__main__':
    print(Solution().subarraySum([-3,1,2,-3,4]))
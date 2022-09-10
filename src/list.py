# create list
#1.
# res = []
# #
# for i in range(10):
#     res.append(i)

#2. list comprehension

# res = [i for i in range(10)]
#
# print(res)

# go through list

# res = [i for i in range(10)]

#1) 位置
# for i in range(len(res)):
#     print(res[i])

#2)　直接拿到value

# for ele in res:
#     print(ele)

#3) 同时拿到所有（位置，value）

# for index, value in enumerate(res):
#     print('index,value : {index}, {v}'.format(index=index,v=value))
#
# string = 'abcdefg'
#
# for index, value in enumerate(string):
#     print('index,value : {index}, {v}'.format(index=index,v=value))

# arraylist, vector: dynamic array, search index -> O(1), append(), add() O(n)
# [ a ] -> [ a, b ] -> [ a, b , , ]
# ａ=1+2
# print(a)

# fun2: num -> 2
# fun: num -> 同一个２
# fun: num -> 5

# def fun(num):
#     num = 5
#
# def fun2():
#     num= 2
#     fun(num)
#     print(num)
#
# fun2()
#
# def fun(lst1):
#     #lst1.append(1)
#     lst1 = [1]
#
# def fun2():
#     lst=[]
#     fun(lst)
#     print(lst)
#
# fun2()

# res = [i for i in range(10)]
# print(res)
# for i in range(len(res)-1,-1,-1):
#     print(res[i])

# range(a,b,c)
# a = start_position
# b = end_position  [a,b)
# c = increase 数量
# range(10) = range(0,10,1)
# range(1,10) = range(1,10,1)

# for i in range(len(res)):
#     print(res[i])

# a=[i for i in range(7)]
# print(a)
#
# print(a[4:])
# print(a[1:4])
# print(a[:-1])
# print(a[:-2])


# def fun(x):
#     x.append(3)
#
#
# def fun2():
#     x=[]
#     fun(x)
#     print(x)
#
# fun2()
#
# class person:
#     def __init__(self,first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def print_full_name(self):
#         print(self.last_name + ', '+self.first_name)

# [] -> list : arraylist
# array : data structure
# array = [1,2,3]
# temp = []
# for i in range(len(array)):
#     temp.append(array[i])
#
# temp.append(4)
# array = temp

# continuous add number into arraylist-> worst case O(n)
# delete O(n)
# search O(1)

#
# def fun(items):
#     # O(n)
#     for item in items:
#         print(item)
#     #O(1)
#     print('hello')
#
#     #O(n)
#     for item in items:
#         print(item)

# fun([1,2,3,4,5,6,7,8])

# O(2n+3*n^0) -> O(2n) -> O(n)
# 1. remove lower power
# 2. remove coefficient
#
#
# def fun1(items):
#     #O(1)
#     result= items[0] * items[0]
#     #O(1)
#     print(result)

#O(2*n^0) -> O(n^0)=O(1)
# fun1([1,2,3,4,5,6,7])
#
#
# def fun1(items):
#     #O(1)
#     result= items[0] * items[0]
#     #O(1)
#     print(result)
#     #O(1)
#     result= items[0] * items[0]
#     #O(1)
#     print(result)
#     #O(1)
#     result= items[0] * items[0]
#     #O(1)
#     print(result)
#     #O(1)
#     result= items[0] * items[0]
#     #O(1)
#     print(result)
#     #O(1)
#     result= items[0] * items[0]

#
#
# def fun2(items):
#     # O(n)
#     for item in items:
#         # O(n)
#         for item2 in items:
#             print('{},{}'.format(item,item2))
#
# fun2([1,2,3,4])
#
#
# def fun3(items):
#     # O(n)
#     for item in items:
#         # O(n)
#         for item2 in items:
#             for item3 in items:
#                 print('{},{},{}'.format(item,item2,item3))
#
#     for item2 in items:
#         for item3 in items:
#             print('{},{},{}'.format(item2, item2, item3))
#
# fun2([1,2,3,4])

# def fun5(items):
#
#     for i in range(len(items)):
#
#         for j in range(i+1,len(items)):
#             print(i,j)
# O(n-1 + n-2 + n-3+....+ 1+ 0)
# fun5([1,2,3,4])

#
# def linear_algo(items):
#
#     # temp = list(items)
#     temp = items
#     temp[0]= 10
#     for item in temp:
#         print(item)
#
# linear_algo([1,2,3,4])
#
# nums = [-1,0,2,3,4,9,12]
#
# def func(nums, target):
#
#     for num in nums:
#         if target == num:
#             return True
#
#     return False
# create list
#1.
# res = []
#
# for i in range(10):
#     res.append(i)

#2. list comprehension

# res = [i for i in range(10)]
#
# print(res)

# string = 'abcdefg'

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

# def fun(num):
#     num = 5
#
# def fun2():
#     num= 2
#     fun(num)
#     print(num)
#
# fun2()

# def fun(lst1):
#     lst1.append(1)
#
# def fun2():
#     lst=[]
#     fun(lst)
#     print(lst)
#
# fun2()
#
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
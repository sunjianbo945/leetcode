
# 图的遍历 Traversal in Graph
# • 层级遍历 Level Order Traversal
# • 由点及面 Connected Component
# • 拓扑排序 Topological Sorting

# 最短路径 Shortest Path in Simple Graph
# • 仅限简单图求最短路径
# • 即,图中每条边长度都是1,且没有方向


# 1. 创建队列，把其实节点放到里面
# 2. while 队列不空，处理队列中的节点，并拓展出新的节点
#   2a. 层级遍历　开始前需要算出每一层size
#   2b. queue

# BFS 图的遍历标配　
# 灌水法
# make graph -> pais to graph or make it to graph
# 2个基友, queue and set

# queue.append(0)
# set.add(0)
#
# while queue:
#     node = queue.pop(0)
#     for neighbor in graph[node]:
#         if neighbor in set:
#             continue
#         set.add(neighbor)
#         queue.append(neighbor)
#
# return len(set) == sizeOfAllNode


# topological sorting
# 1. indegree　入度
# 2. select free element
# 3. for each free element's neighbor decrease by 1, if the node becomes 0, add into the result

#
#
# • 能用 BFS 的一定不要用 DFS(除非面试官特别要求)
# • BFS 的两个使用条件
# • 图的遍历(由点及面,层级遍历)
# • 简单图最短路径
# • 是否需要层级遍历
# •
# size = queue.size()
# • 拓扑排序必须掌握!
# • 坐标变换数组
# • deltaX, deltaY
# • inBound

# https://stomachache007.wordpress.com/2017/03/20/nc4-md/

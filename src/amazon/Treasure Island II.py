# You have a map that marks the locations of treasure islands. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest route to one of the treasure islands.
#
# Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from one of the starting point (marked as S) of the map and can move one block up, down, left or right at a time. The treasure island is marked as X. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. Output the minimum number of steps to get to any of the treasure islands.
#
# Example:
#
# Input:
# [['S', 'O', 'O', 'S', 'S'],
#  ['D', 'O', 'D', 'O', 'D'],
#  ['O', 'O', 'O', 'O', 'X'],
#  ['X', 'D', 'D', 'O', 'O'],
#  ['X', 'D', 'D', 'D', 'O']]
#
# Output: 3
# Explanation:
# You can start from (0,0), (0, 3) or (0, 4). The treasure locations are (2, 4) (3, 0) and (4, 0). Here the shortest route is (0, 3), (1, 3), (2, 3), (2, 4).

def find(matrix):

    queue = []
    visited=set()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'S':
                queue.append((i,j))
                visited.add((i,j))


    direction=[[-1,0],[1,0],[0,1],[0,-1]]
    total = 0
    while queue:

        size = len(queue)

        for i in range(size):
            x,y = queue.pop(0)
            if matrix[x][y]=='X':return total
            for d in direction:
                n_x,n_y = x+d[0],y+d[1]

                if v(matrix,n_x,n_y,visited):
                    queue.append((n_x,n_y))
                    visited.add((n_x,n_y))

        total +=1

    return -1


def v(matrix,x,y,visited):
    return x>=0 and y>=0 and x<len(matrix) and y<len(matrix[0]) and (x,y) not in visited and matrix[x][y]!='D'



print(find(
[['S', 'O', 'O', 'S', 'S'],
 ['D', 'O', 'D', 'O', 'D'],
 ['O', 'O', 'O', 'O', 'X'],
 ['X', 'D', 'D', 'O', 'O'],
 ['X', 'D', 'D', 'D', 'O']]

))















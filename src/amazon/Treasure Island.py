# You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest route to the treasure island.
#
# Assume the map area is a two dimensional grid, represented by a matrix of characters.
# You must start from the top-left corner of the map and can move one block up, down, left or right at a time.
# The treasure island is marked as X in a block of the matrix. X will not be at the top-left corner.
# Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in.
# The top-left corner is always safe. Output the minimum number of steps to get to the treasure.
#
# Example:
#
# Input:
# [['O', 'O', 'O', 'O'],
#  ['D', 'O', 'D', 'O'],
#  ['O', 'O', 'O', 'O'],
#  ['X', 'D', 'D', 'O']]
#
# Output: 5
# Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.


def find(matrix):

    queue = [(0,0)]

    visited={(0,0)}

    direction = [[0,1],[0,-1],[-1,0],[1,0]]
    total = 0

    while queue:

        size = len(queue)

        for i in range(size):

            x,y = queue.pop(0)
            if matrix[x][y]=='X':
                return total
            for d in direction:
                n_x,n_y = x+d[0],y+d[1]

                if validate(matrix,n_x,n_y,visited):
                    queue.append(((n_x,n_y)))
                    visited.add((n_x,n_y))

        total+=1




def validate(matrix,x,y,visited):

    return x>=0 and y >=0 and x<len(matrix) and y<len(matrix[0]) and matrix[x][y]!='D' and (x,y) not in visited


print(find(
[['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]
))























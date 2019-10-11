class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """

    def minArea(self, image, x, y):
        # write your code here

        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        queue = [(x, y)]
        visited = set()
        visited.add((x, y))

        min_x, max_x = x, x
        min_y, max_y = y, y

        while queue:

            node = queue.pop(0)
            print(node)
            for d in direction:

                new_x, new_y = node[0] + d[0], node[1] + d[1]

                if not self.check_boundary(image, new_x, new_y):
                    continue

                if (new_x, new_y) not in visited and image[new_x][new_y] == '1':
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))
                    min_x, max_x = min(min_x, new_x), max(max_x, new_x)
                    min_y, max_y = min(min_y, new_y), max(max_y, new_y)

        return (max_x - min_x + 1) * (max_y - min_y + 1)

    def check_boundary(self, image, x, y):
        return x >= 0 and y >= 0 and x < len(image) and y < len(image[0])


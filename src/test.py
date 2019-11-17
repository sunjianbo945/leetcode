google_news_url = "https://news.google.com/news/rss"
import requests
#
#
# def get_headlines(rss_url):
#     """
#     @returns a list of titles from the rss feed located at `rss_url`
#     """
#     response = requests.get(rss_url)
#
#     if response.status_code != 200:
#         raise Exception(f'request has eroor {rss_url} can not get response with error code {response.status_code}')
#
#     content = response.text
#     res = []
#     for index, value in enumerate(content):
#
#         if value == '<' and index + 7 <= len(content) and content[index:index + 7] == '<title>':
#             title = extract_title(content, index + 7)
#             res.append(title)
#
#     return res[1:]
#
#
# def extract_title(content, index):
#     if index >= len(content):
#         return ''
#
#     res = ''
#     for i in range(index, len(content)):
#         if content[i] == '<' and i + 8 <= len(content) and content[i:i + 8] == '</title>':
#             return res
#         res += content[i]
#
#     return res
#
#
# print(get_headlines(google_news_url))

# def s(A):
#
#     temp = find_min(A)
#
#     res = 1
#
#     for i in range(1,len(temp)):
#         if temp[i]!=temp[i-1]:
#             res+=1
#
#     return res
#
#
# def find_min(A):
#     res = [len(A) - 1] * len(A)
#
#     min_num = A[-1]
#
#     for i in range(len(A) - 2, -1, -1):
#
#         if A[i] < min_num:
#             res[i] = i
#             min_num = A[i]
#         else:
#             res[i] = res[i + 1]
#
#     return res
#
# print(s([2, 4, 1, 6, 5, 9, 7]))

# !/bin/python3

import sys


# Complete the function below.
class BlobFinder:

    def __init__(self, blob):
        self.blob = blob
        self.top = 0
        self.left = 0
        self.right = len(blob[0])
        self.bottom = len(blob)
        self.totalRead = 0

    def _findTop(self):

        for i in range(self.bottom):
            for j in range(self.left, self.right):
                self.totalRead += 1
                if self.blob[i][j] == 1:
                    self.top = i
                    self.left = j
                    return i

        return -1


    def _findBottom(self):
        for i in range(self.bottom - 1, -1, -1):
            for j in range(self.right-1, self.left-1,-1):
                self.totalRead += 1
                if self.blob[i][j] == 1:
                    self.right = j
                    self.bottom = i
                    return

    def _findLeft(self):
        most_left = self.right

        for i in range(self.top+1, self.bottom ):
            for j in range(most_left):
                self.totalRead += 1
                if self.blob[i][j] == 1:
                    most_left = min(j, most_left)
                    break

        self.left = most_left
        return most_left

    def _findRight(self):
        most_right = self.left

        for i in range(self.top+1, self.bottom):
            for j in range(self.right, most_right, -1):
                self.totalRead += 1
                if self.blob[i][j] == 1:
                    most_right = max(j, most_right)
                    break

        self.right = most_right
        return most_right

    def findBoundary(self):
        self._findTop()
        self._findBottom()
        self._findLeft()
        self._findRight()


def getBlobBoundaries(inputGrid):
    finder = BlobFinder(inputGrid)
    finder.findBoundary()

    print('Cell Reads:{}'.format(finder.totalRead))
    print('Top:{}'.format(finder.top))
    print('Left:{}'.format(finder.left))
    print('Right:{}'.format(finder.right))
    print('Bottom:{}'.format(finder.bottom))


if __name__ == "__main__":
    inputGrid_rows = 0
    inputGrid_cols = 0
    inputGrid_rows = int(input())
    inputGrid_cols = int(input())

    inputGrid = []
    for inputGrid_i in range(inputGrid_rows):
        inputGrid_temp = [int(inputGrid_t) for inputGrid_t in input().strip().split(' ')]
        inputGrid.append(inputGrid_temp)

    res = getBlobBoundaries(inputGrid);

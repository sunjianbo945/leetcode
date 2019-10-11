class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        matrix = self.palindrome_matrix(s)
        res = []
        self.recur(s,0,[],res,matrix)
        return res

    def recur(self, s, start, cur, res,matrix):

        if start>=len(s):
            res.append(cur)
            return

        for i in range(start,len(s)):
            if matrix[start][i]:
                self.recur(s,i+1,cur+[s[start:i+1]],res,matrix)



    def palindrome_matrix(self, s):

        matrix = [[False for _ in s] for _ in s]
        # initialization
        for i in range(len(s)):
            matrix[i][i] = True
            if i<len(s)-1:
                matrix[i][i+1] = s[i]==s[i+1]

        for i in range(len(s)-3,-1,-1):
            for j in range(i+2,len(s)):

                matrix[i][j] = matrix[i+1][j-1] and s[i]==s[j]

        # print(matrix)

        return matrix
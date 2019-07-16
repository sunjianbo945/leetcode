class Solution(object):
    def generateParenthesis(self, n):

        def paren(left, right, curr, res):
            # 'evaluate current string
            # if we are out of brackets to add, we must be at a valid string
            if left == 0 and right == 0:
                res.append(curr)
                return

            # recursive call: add either open or close
            # if adding open bracket is valid
            if left > 0:
                # add open bracket, decr count
                paren(left - 1, right, curr + "(", res)

            # if adding close bracket is valid
            if right > left:
                # add close bracket, decr count
                paren(left, right - 1, curr + ")", res)

            return res

        # end paren()

        res = paren(n, n, '', [])

        return res


def main():
    print(Solution().generateParenthesis(3))

if __name__=='__main__':
    main()
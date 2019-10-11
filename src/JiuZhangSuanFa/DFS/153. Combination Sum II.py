class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """

    def combinationSum2(self, candidates, target):
        # write your code here
        res = []

        self.recur(sorted(candidates), 0, [], target, res)
        return res

    """
    @param candidates: A list of integers
    @param index: An integer indicates the index of the number in the candidates list
    @param cur: The existing list that may achive the goal
    @param target: An integer
    """

    def recur(self, candidates, index, cur, target, res):

        if target == 0:
            res.append(cur)

        if index >= len(candidates) or target < 0:
            return

        for i in range(index, len(candidates)):

            if i != index and candidates[i] == candidates[i - 1]:
                continue

            self.recur(candidates, i + 1, cur + [candidates[i]], target - candidates[i], res)
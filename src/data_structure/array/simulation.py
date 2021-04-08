# https://leetcode.com/problems/dota2-senate/
class Solution649:
    def predictPartyVictory(self, senate: str) -> str:
        radiant, dire = [], []
        n = len(senate)
        for idx, s in enumerate(senate):
            if s == 'R':
                radiant.append(idx)
            else:
                dire.append(idx)

        while radiant and dire:
            r, d = radiant.pop(0), dire.pop(0)
            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)

        return 'Radiant' if radiant else 'Dire'


# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
class Solution1342:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        while num:
            num, r = divmod(num, 2)
            if r == 1:
                step += 1

            if num != 0:
                step += 1

        return step

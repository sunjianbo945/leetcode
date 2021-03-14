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
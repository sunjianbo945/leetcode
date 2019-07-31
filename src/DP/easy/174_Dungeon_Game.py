from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows = len(dungeon)
        columns = len(dungeon[0])
        hp_memo= [ [0]*columns for _ in range(rows)]
        hp_memo[-1][-1] = dungeon[-1][-1] if dungeon[-1][-1]<0 else 0

        for i in range(len(dungeon[0])-2,-1,-1):
            num = hp_memo[-1][i+1] + dungeon[-1][i]
            hp_memo[-1][i] = num if num<0 else 0

        for i in range(len(dungeon)-2,-1,-1):
           num = hp_memo[i+1][-1] + dungeon[i][-1]
           hp_memo[i][-1] = num if num<0 else 0


        for i in range(len(dungeon)-2,-1,-1):
            for j in range(len(dungeon[0])-2,-1,-1):
                num = max(hp_memo[i+1][j],hp_memo[i][j+1] )+ dungeon[i][j]
                hp_memo[i][j] = num if num<0 else 0

        if hp_memo[0][0]<0:
            return hp_memo[0][0] * (-1) +1
        else:
            return 1



def main():
    print(Solution().calculateMinimumHP([[1,3,1],[1,5,1],[4,2,1]]))


if __name__=='__main__':
    main()
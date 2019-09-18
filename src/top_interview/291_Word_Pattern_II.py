
# Example 1:
#
# Input: pattern = "abab", str = "redblueredblue"
# Output: true
#
# Example 2:
#
# Input: pattern = pattern = "aaaa", str = "asdasdasdasd"
# Output: true
#
# Example 3:
#
# Input: pattern = "aabb", str = "xyzabcxzyabc"
# Output: false



class Solution:

    def wordPatternMatch(self,pattern:str, string:str):
        m = {}
        b = self.dfs(pattern, 0, string, 0, m, set())
        return b

    def dfs(self,pattern,pattern_idx, string,string_idx, memo,val_set):

        if pattern_idx == len(pattern) and string_idx == len(string): return True
        if pattern_idx == len(pattern) or string_idx == len(string): return False

        char = pattern[pattern_idx]

        if char in memo:

            char_val = memo[char]
            if string_idx+len(char_val)>len(string):
                return False

            if string[string_idx:string_idx+len(char_val)] == char_val:
                return self.dfs(pattern,pattern_idx+1,string,string_idx+len(char_val),memo,val_set)

        else:

            for i in range(string_idx,len(string)):
                if string[string_idx:i+1] not in val_set:
                    val_set.add(string[string_idx:i+1])
                    memo[char] =string[string_idx:i+1]
                    if self.dfs(pattern,pattern_idx+1,string,i+1,memo,val_set):
                        return True
                    else:
                        val_set.remove(string[string_idx:i+1])
                        del memo[char]

            return False


if __name__=='__main__':
    print(Solution().wordPatternMatch('abab','redblueredblue'))
    print(Solution().wordPatternMatch('aaaa','asdasdasdasd'))
    print(Solution().wordPatternMatch('aabb','xyzabcxyzabc'))
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        word_dict = {}
        res = 0
        index = 0
        while index<len(s):
            if s[index] not in word_dict or word_dict[s[index]] < start:
                pass
            else:
                temp = word_dict[s[index]]
                res = max(res, index - start)
                start = temp+1

            word_dict[s[index]] = index
            index+=1

        return max(res, index-start)



def main():
    print(Solution().lengthOfLongestSubstring("abcabccc"))


if __name__=='__main__':
    main()
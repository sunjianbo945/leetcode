class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        res = []
        for i in range(len(logs)):
            log_detials = logs[i].split(' ')

            if log_detials[1].isalpha():
                res.append((0, ' '.join(log_detials[1:]), logs[i]))
            else:
                res.append((1, i, logs[i]))

        res.sort()

        return [i[2] for i in res]


print(Solution().reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
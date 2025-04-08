# https://leetcode.com/problems/score-of-a-string/solutions/5104009/score-of-a-string/

class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        score = 0
        for index in range(1,len(s)):
            score += abs(ord(s[index-1]) - ord(s[index]))
        return score
# https://leetcode.com/problems/valid-anagram/

# TC: O(n log n + m log m) (or O(n log n) if n ≈ m)

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
        
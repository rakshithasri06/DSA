class Solution(object):
    def rotateString(self, s, goal):
        c=0
        for i in range(len(s)):
            if s[i]==goal[0]:
                c=i
            if goal==s[c:]+s[:c]:
                return True
        return False
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        
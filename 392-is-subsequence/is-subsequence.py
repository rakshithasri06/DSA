class Solution(object):
    def isSubsequence(self, s, t):
        c=0
        for i in s:
            if i in t:
                c=c+1
                t=t[t.index(i)+1:]
        if len(s)==c:
            return (True)
        else:
            return (False)
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
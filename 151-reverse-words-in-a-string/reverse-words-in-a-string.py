class Solution(object):
    def reverseWords(self, s):
        l=list(s.split())
        s=''
        for i in range(len(l),0,-1):
            s=s+ l[i-1]+" "
        return s.rstrip()

        """
        :type s: str
        :rtype: str
        """
        
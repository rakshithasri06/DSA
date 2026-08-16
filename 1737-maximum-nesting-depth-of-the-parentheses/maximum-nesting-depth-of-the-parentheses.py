class Solution(object):
    def maxDepth(self, s):
        counter=maxcounter=0
        for i in s:
            if i=="(":
                counter+=1
            elif i==")":
                maxcounter=max(counter,maxcounter)
                counter-=1
        return maxcounter
        """
        :type s: str
        :rtype: int
        """
        
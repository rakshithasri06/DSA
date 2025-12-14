class Solution(object):
    def maxVowels(self, a, k):
        window_max=c=0
        for i in range(0,len(a[:k])):
            if a[i] in "aeiou":
                c=c+1
        window_max=c
        for j in range(k,len(a)):
            if a[j-k] in "aeiou":
                c=c-1
            if a[j] in "aeiou":
                c=c+1
            else:
                pass
            window_max=max(c,window_max)
        return(window_max)
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
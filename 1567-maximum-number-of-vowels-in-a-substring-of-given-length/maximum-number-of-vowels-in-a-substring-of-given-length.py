class Solution(object):
    def maxVowels(self, s, k):
        l=0
        r=k
        n=s[l:r]
        c=0
        maxi=0
        for i in n:
            if i in "aeiou":
                c=c+1
            maxi=c
        while r<len(s):
            if s[l] in "aeiou":
                c-=1
            if s[r] in "aeiou":
                c+=1
            l+=1
            r+=1
            maxi=max(maxi,c)
        return maxi

            
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
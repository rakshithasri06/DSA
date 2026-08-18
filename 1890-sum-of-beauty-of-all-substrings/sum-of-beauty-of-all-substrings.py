class Solution(object):
    def beautySum(self, s):
        ans=0
        for i in range(len(s)):
            freq=[0]*26
            for j in range(i,len(s)):
                freq[ord(s[j])-ord('a')]+=1
                maxfreq=max(freq)
                minfreq=float('inf')
                for x in freq:
                    if x>0 :
                        minfreq=min(minfreq,x)
                ans+=maxfreq-minfreq
        return ans
        """
        :type s: str
        :rtype: int
        """
        
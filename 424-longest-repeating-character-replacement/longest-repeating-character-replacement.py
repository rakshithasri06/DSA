class Solution(object):
    def characterReplacement(self, s, k):
        left=0
        count_freq={}
        res=0

        maxf=0

        for right in range(len(s)):
            count_freq[s[right]]=1+count_freq.get(s[right],0)
            maxf=max(maxf,count_freq [s[right]])

            while ((right-left+1) - maxf) > k:
                count_freq[s[left]]-=1
                left+=1
                
            res=max(res,right-left+1)
        
        return(res)


        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
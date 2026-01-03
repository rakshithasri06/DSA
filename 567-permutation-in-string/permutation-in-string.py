class Solution(object):
    def checkInclusion(self, s1, s2):

        left=0
        count1={}
        count2={}

        for i in range(len(s1)):
            count1[s1[i]]=1+count1.get(s1[i],0)
        print(count1)
        window=s2[:len(s1)]


        for j in range(len(window)):
            count2[window[j]]=1+count2.get(window[j],0)

        if count1==count2:
            return True
            
            
        for right in range(len(s1),len(s2)):
            count2[s2[right]]=1+count2.get(s2[right],0)
            
            count2[s2[left]]-=1
            if count2[s2[left]] == 0:
                del count2[s2[left]]
            left+=1
            window=s2[left:right]
            
            if count1==count2:
                return True



        return False
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
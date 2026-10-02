class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        dic = {}

        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            if stack:
                dic[nums2[i]] = stack[-1]
            else:
                dic[nums2[i]] = -1

            stack.append(nums2[i])

        res = []

        for num in nums1:
            res.append(dic[num])

        return res
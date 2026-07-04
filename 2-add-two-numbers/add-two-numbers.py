# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        current=l1
        st1=""
        st2=""
        while current:
            st1+=str(current.val)
            current=current.next
        str1=st1[::-1]
        current=l2
        while current:
            st2+=str(current.val)
            current=current.next
        str2=st2[::-1]

        n=str(int(str1)+int(str2))[::-1]
        head=None
        current=None

        for digits in n:
            node=ListNode(int(digits))
            if head is None:
                head = node
                current = node
            else:
                current.next = node
                current = node

        return head






        
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
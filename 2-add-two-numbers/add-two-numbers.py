# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy=ListNode(0)
        current=dummy
        carry=0
        while l1 or l2 or carry:
            x=l1.val if l1 else 0
            y=l2.val if l2 else 0
            sums=x+y+carry
            digit=sums%10
            carry=sums//10
            current.next=ListNode(digit)
            current=current.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next

        return dummy.next

        '''
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
        '''






        
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
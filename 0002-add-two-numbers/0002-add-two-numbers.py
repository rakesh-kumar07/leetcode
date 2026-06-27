# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        current=dummy
        carry=0

        while l1 or l2 or carry:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            total=val1+val2+carry

            carry=total//10
            current.next=ListNode(total%10)
            current=current.next

            if l1:l1=l1.next
            if l2:l2=l2.next
        return dummy.next

        # l1.sorted(reverse=True)
        # l2.sorteed(reverse=True)
        # for i,j in zip(l1,l2):
        #     sum[i]=(l1[i]+l2[j]+rem[i])%10
        #     rem[i]=(l1[i]+l2[j])/10
        # return sum.sorted(reverse=True)
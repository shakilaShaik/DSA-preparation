# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1=list1
        current2=list2
        new_list=ListNode()
        current=new_list
    
        
        while(current1 and current2):
            if current1.val < current2.val:
                
                current.next=ListNode(current1.val)
                current1=current1.next
                current=current.next
            else:
                current.next=ListNode(current2.val)
                current2=current2.next
                current=current.next
        while(current1):
            current.next=ListNode(current1.val)
            current1=current1.next
            current=current.next
        while(current2):
            current.next=ListNode(current2.val)
            current2=current2.next
            current=current.next
        return new_list.next

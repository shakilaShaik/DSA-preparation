# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_begin(self,data):
        
        new_node=Node(data)
        if self.head=None:
            self.head=new_node   // if there is no node present
            return
        new_node.next=self.head
        self.head=new_node
    def insert_at_end(self,data):
        new_node=Node(data)
        if new_node.next==None:
            new_node.next=self.head
            self.head=new_node
        temp=self.head
        temp.next=new_node
    def del_node(self,key):
        
        temp=self.head
        if temp and temp.data==key:
            self.head=temp.next
            temp=None
            return
        prev=None
        while temp and temp.data !=key:
            prev=temp
            temp=temp.next
            if temp is None:
                return 
            prev.next=temp.next
            temp=None
    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
shammu_ll=LinkedList()
shammu_ll.insert_at_begin(22)
shammu_ll.insert_at_begin(24)
shammu_ll.insert_at_begin(26)
shammu_ll.insert_at_begin(28)
shammu_ll.print_list()




from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MySumList:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = x + y + carry

            carry = total // 10
            value = total % 10
            current.next = ListNode(value)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next

# Helper function: Convert list → linked list
def list_to_linked(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function: Convert linked list → list
def linked_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# Example usage:
myObj = MySumList()
l1 = list_to_linked([1,5,7])
l2 = list_to_linked([1,4,2])
res = myObj.addTwoNumbers(l1, l2)

print(linked_to_list(res))  # [2, 9, 9]

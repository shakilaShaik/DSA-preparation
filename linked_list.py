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


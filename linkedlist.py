class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked:
    def __init__(self):
        self.head=None
        self.index=None
    def insertAtFirst(self,data):
        node=Node(data)
        if self.head==None:
            self.head=node
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=node
    def display(self):
        temp=self.head
        while temp!=None:
         print(temp.data,end=" ")
         temp=temp.next
    def deleteAttFirst(self):
        self.head=self.head.next
    def insertfirst(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node
    def insertAtMid(self,index,data):
        node=Node(data)
        temp=self.head
        if index==0:
            self.insertfirst(data)
        else:
         for i in range(0,index):
            temp=temp.next
         node.next=temp.next
         temp.next=node

    def deletelast(self):
        temp=self.head
        while temp.next.next!=None:
            temp=temp.next
        temp.next=None

list=linked()
list.insertAtFirst(3)
list.insertAtFirst(1)
list.insertAtFirst(7)
list.insertAtMid(0,6)
list.display()
print()
list.display()










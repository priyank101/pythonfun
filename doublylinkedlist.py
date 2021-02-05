class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class linked:
    def __init__(self):
        self.head=None
    def insert(self,data):
        node = Node(data)
        if self.head is None:
            self.head=node
        else:
            node.next=self.head
            self.head.prev=node
            self.head=node

    def insertL(self,data):
        node=Node(data)
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=node
        node.prev=temp

    def insertM(self,index,data):
        node=Node(data)
        temp=self.head
        if index==0:
            self.insert(data)
        else:
         for i in range(0,index):
            temp=temp.next
         node.next=temp.next
         node.prev=temp
         temp.next=node


    def deleteL(self):
        temp=self.head
        while temp.next.next!=None:
            temp=temp.next
        temp.next=None

    def print(self):
        if self.head is None:
           print("empty list")
        else:
            temp=self.head
            while temp!=None:
             print(temp.data,end=" ")
             temp=temp.next

lst=linked()
lst.insert(2)
lst.insert(1)
lst.insert(3)
lst.insertL(8)
lst.insertM(0,5)
lst.print()

































































































































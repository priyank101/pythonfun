class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.root=data

    def insert(self,data):
        node=Node(data)
        if self.root:
            if data<self.root:
                if self.left is None:
                    self.left=node
                else:
                    self.left.insert(data)
            elif data>self.root:
                if self.right is None:
                    self.right=node
                else:
                    self.right.insert(data)
        else:
            self.root=data

    def print(self):
        if self.left:
            self.left.print()
        print(self.root,end=" ")
        if self.right:
            self.right.print()
    def preorder(self,tree):
        lst = []
        if tree:
         lst.append(tree.root)
         lst=lst+ self.preorder(tree.left)
         lst=lst+self.preorder(tree.right)
        return lst
    def search(self,val):
        if val<self.root:
            if self.left is None:
                return str(val)+ " is not found"
            return self.left.search(val)
        elif val>self.root:
            if self.right is None:
                return str(val)+ " is not found"
            return self.right.search(val)
        else:
            return (str(self.root)+ ' is found')

tree=Node(10)
tree.insert(1)
tree.insert(2)
tree.insert(7)
tree.insert(11)
tree.insert(12)
tree.insert(14)
tree.insert(17)
tree.print()
print()
#rint(tree.preorder(tree))
print(tree.search(7))
#print(tree.inorder(tree))
#print(tree.postorder(tree))


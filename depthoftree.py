class Node:
    def __int__(self,key):
        self.data=key
        self.left=None
        self.right=None

    def function(self,root):
        if root is None:
            return 0
        else:
            ldepth=self.function(root.left)
            rdepth=self.function(root.right)
            if ldepth > rdepth:
                return ldepth+1
            else:
                return rdepth+1

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.function()
class Node:
    def __init__(self,key):
        self.data=key
        self.left=None
        self.right=None
    def function(root):
        if root is None:
            return
        queue=[]
        queue.append(root)
        m=[]
        while len(queue) > 0:
            #print(queue[0].data,end=" ")
            m.append(queue[0].data)
            node=queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        for i in range(len(m)-1,-1,-1):
            print(m[i],end=" ")
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.right.left=Node(5)
root.function()


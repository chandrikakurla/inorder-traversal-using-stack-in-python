#class to create nodes of a tree
class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
#function to inorder traversal of a tree 
def print_Inorder(root):
    #initialising stack
    stack=[]
    currentnode=root
    while True:
        #reach leftmost node of current
        if currentnode is not None:
            stack.append(currentnode)
            currentnode=currentnode.left
        elif(stack):
            currentnode=stack.pop()
            print(currentnode.data,end=" ")
            currentnode=currentnode.right
        else:
            #if currentnode is none and stack is empty then traversal is completed
            break
#main programme
if __name__=="__main__":
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    root.right.left=Node(6)
    root.right.right=Node(7)
    print("Inorder traversal of tree is:")
    print_Inorder(root)



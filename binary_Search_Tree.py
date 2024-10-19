# binary tree program application

# class Node:
#     def __init__(self, data) -> None:
#         self.leftChild = None
#         self.key = data
#         self.rightChild = None


# class BST:
#     def __init__(self) -> None:
#         self.root = None
#         self.current_node = None

#     def add_node(self, data):
#         # check if the tree is empty
#         if self.root == None:
#             self.root = Node(data)
#             return
#         else:
#             self.current_node = self.root
#             while True:
#                 if self.current_node.key < data:
#                     if self.current_node.rightChild is None:
#                         self.current_node.rightChild = Node(data)
#                         break
#                     else:
#                         self.current_node = self.current_node.rightChild
#                 else:
#                     if self.current_node.leftChild is None:
#                         self.current_node.leftChild = Node(data)
#                         break
#                     else:
#                         self.current_node = self.current_node.leftChild

class BST:
    def __init__(self, key):
        self.rChild = None
        self.key = key
        self.lChild = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key > data:
            if self.lChild is not None:
                self.lChild.insert(data)
            else:
                self.lChild = BST(data)
        else:
            if self.rChild is not None:
                self.rChild.insert(data)
            else:
                self.rChild = BST(data)


BST1 = BST(None)

for n in [100, 50, 110, 55, 108, 103, 45]:
    BST1.insert(n)





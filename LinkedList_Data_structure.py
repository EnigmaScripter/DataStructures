# There are three types of linked lists
#       1- Singly linked List => simple linked list.
#       2- Doubly Linked list.
#       3- circulor Linked list.
# Singly linked list is the simplest linked list.
# Each node of the singly linked list contains one link for the coming node
# The last link of the last node is null.
# Direction is this type of liked list is not easy as each node has one link to the upcoming Node
# So, node does not know about the previous node

# Adding or insertion in a linked list mean we have to break the link
# we add item at the begianing, end or in-between linked list.

class Node: 
    def __init__(self, data) -> None:
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def print_LL(self, head): # Printing Linked List items till the ref is none
        if self.head is None:
            print("Linked list is empty!!")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
    # A method to add node at the begaining of the linked list
    def add_begin(self, data): 
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    # Adding item at the end of lined list
    def add_Ending(self, data):
        new_node = Node(data)
        print(f"we created a new node with data {new_node.data} and ref {new_node.ref}")
        if self.head is None: # check if the head of the Linked list is none means the list is empty
            print(f"we checked if the self.head is none which means the linked list is empty => self head is {self.head}")
            self.head = new_node 
        else:                                # if the Linked list head is not empty
            n = self.head                    # set n equal to the self head
            while n.ref is not None:         # do loop till the head is empty
                print(f"the node ref is not none which means it is not the end og the linked list => Node Data {n.data} Node ref {n.ref} ")
                n = n.ref                    # if the head is not empty will set the n to the coming node ref and check
            else:                            # if the head is empty 
                print(f"the node ref is none here, so it is the end of the linked list => Node Data {n.data} Node ref {n.ref} ")
                n.ref = new_node # set line of the empty node to the new node

    def add_BeforeNode(self, data, x):
        if self.head is None:
            print("the linked list is empty!!")
        else:
            new_node = Node(data)
            n = self.head
            while n is not None:
                if n.data == x:
                    new_node.ref = n.ref
                    n.ref = new_node
                    break
                else:
                    n = n.ref


    def add_AfterNode(self, data, x):
        if self.head is None:
            print("the linked list is empty!!")
        else:
            new_node = Node(data)
            n = self.head
            while n is not None:
                if n.data == x:
                    new_node.ref = n
                    prev_node.ref = new_node
                    break
                else:
                    prev_node = n
                    n = n.ref



LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(30)
LL1.add_begin(40)
LL1.add_begin(50)
LL1.add_begin(60)
LL1.add_Ending(70)
LL1.add_AfterNode(45, 40)
LL1.add_BeforeNode(35, 40)
LL1.add_BeforeNode(15, 20)

LL1.print_LL(LL1)

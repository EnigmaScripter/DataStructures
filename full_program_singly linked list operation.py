# this is an application to practice singly linked list operations.
# will practice lionked list operations which are Add and Delete

import termcolor
import pyfiglet

print(termcolor.colored(pyfiglet.figlet_format("Linked List"), "yellow"))

# The class Node to create a new node
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.ref = None

# class to create a new linked list
class Singly_Linked_List:
    # Head intiation => to keep the head of the linked list
    def __init__(self) -> None:
        self.head = None

    # Method to print all the list nodes
    def print_List(self):
        if self.head is None:
            print("The linked list is empty!!")
        else:
            n = self.head
            while n is not None :
                print(f"{n.data} ==>", end=" ")
                n = n.ref
        print("\n")
        print("=" * 60)

    
    # Method to check if the linked list is empty.
    def is_Empty_List(self):
        if self.head is None:
            print("The linked list is Empty!!")
            print("=" * 60)
        else:
            print("The Linked list is not empty")
            print("=" * 60)            

    # A method to add node at the begaining of the linked list
    def add_begian(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    

    def add_End(self, data):
        # Check if thw linked List is empty
        if self.head is None:
            print("The linked list is empty!!") 
        else:
            new_node = Node(data)
            n = self.head
            while n.ref is not None:
                n = n.ref
            else:
                n.ref = new_node


    def add_before(self, data, x):
        new_node = Node(data)
        if self.head is None:
            print("The linked list is empty!!") 
        else:
            n = self.head
            while n.ref is not None:
                if x == n.data:
                    new_node.ref = n.ref
                    n.ref = new_node
                    break
                else:
                    n = n.ref
                
    def add_After(self, data, x):
        new_node = Node(data)
        n = self.head
        afterNode = None
        if self.head is None:
            print("The linked list is empty!!") 
        else:
            while n.ref is not None:
                if x == n.data:
                    afterNode.ref = new_node
                    new_node.ref = n
                    break
                else:
                    afterNode = n
                    n = n.ref


    def del_Begian(self):
        if self.head is None:
            print("The Linked list is Empty!!")
            print("=" * 60)
        else:
            n = self.head
            self.head = self.head.ref
            n.ref = None
            print(f"Begaining node which is {n.data} has been deleted successfully!!")
            print("=" * 60)

    def del_End(self):
        if self.head is None:
            print("The Linked list is Empty!!")
            print("=" * 60)
        else:
            n = self.head
            while n.ref is not None:
                beforeNode = n
                n = n.ref
            else:
                beforeNode.ref = None
                print(f"Ending node which is {n.data} has been deleted successfully!!")
                print("=" * 60)

    def del_Node(self, data):
        if self.head is None:
            print("The Linked list is Empty!!")
            print("=" * 60)
        else:
            n = self.head
            while n is not None:
                if data == n.data:
                    beforeNode.ref = n.ref
                    n.ref = None
                    break
                else:
                    beforeNode = n
                    n = n.ref

    def items_Count(self) -> int:
        if self.head is not None:
            counter = 0
            n = self.head
            while n is not None:
                counter += 1
                n = n.ref
            return counter
    
    def Clear_List(self):
        if self.head is None:
            print("Linked List is Empty!!")
            print("=" * 60)

        else:
            n = self.head
            while n is not None:
                self.head = n.ref
                n.ref = None
                n = self.head
            print("Linked list cleared Successfully!!")

LL1 = Singly_Linked_List()

while True:
    user_selection = int(input("""Please select the action needed 
                               1 => Add node.
                               2 => Delete node.
                               3 => check empty.
                               4 => print list nodes.
                               5 => Linked list Nodes count.
                               6 => Clear Linked List.
                               7 => Quite The app. \n"""))
    
    print("=" * 60)
    if user_selection == 1: 
        while True:
            second_selection = int(input("1 => Add node at the begaining \n2 => Add node at the end \n3 => Add befor specific Node \n4 => Add after specific node \n5=> Go to the main menu \n"))
            if second_selection == 1:
                data = int(input("Please enter the node data: "))
                LL1.add_begian(data)
                LL1.print_List()

            elif second_selection == 2:
                data = int(input("Please enter the node data: "))
                LL1.add_End(data)
                LL1.print_List()

            elif second_selection == 3:
                data = int(input("Please enter the node data: "))
                x = int(input("Please add the specific node data: "))
                LL1.add_before(data, x)
                LL1.print_List()

            elif second_selection == 4:
                data = int(input("Please enter the new node data: "))
                x = int(input("Please add the specific node data: "))
                LL1.add_After(data, x)
                LL1.print_List()

            elif second_selection == 5:
                break

    elif user_selection == 2:
        while True:
            second_selection = int(input("1 => Delete node at the begaining \n2 => Delete node at the end \n3 => Delete Node by value \n4=> Go to the main menu \n"))
            if second_selection == 1: 
                LL1.del_Begian()
                LL1.print_List()
            elif second_selection == 2:
                LL1.del_End()
                LL1.print_List()
            elif second_selection == 3:
                data = int(input("Pleaser enter the Node value that you want to delete: "))
                LL1.del_Node(data)
                LL1.print_List()
            elif second_selection == 4:
                break

    elif user_selection == 3:
        LL1.is_Empty_List()
    elif user_selection == 4:
        LL1.print_List()
    elif user_selection == 5:
        counter = LL1.items_Count()
        if counter is None:
            print("Linked List is Empty!!")
            print("=" * 60)
        else:
            print(f"linked list items count is {counter}")
            print("=" * 60)
    elif user_selection == 6:
        LL1.Clear_List()
    elif user_selection == 7:
        print("=" * 60)
        print("Thanks for using my app")
        print("=" * 60)
        exit()






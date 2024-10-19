# This a full application for Doubly Linked list


import termcolor
import pyfiglet

print(termcolor.colored(pyfiglet.figlet_format("Doubly Linked List"), "yellow"))

class Node:
    def __init__(self, data) -> None:
        self.pref = None
        self.data = data
        self.nref = None

class Doubly_Linked_list:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def print_List(self):
        if self.head is None:
            print(termcolor.colored("Linked List is empty!!", "red")) 
        else:
            n = self.head
            while n is not None:
                print(termcolor.colored(f"{n.data} ==>", "light_blue"), end= " ")
                n = n.nref

    def reverse_print_List(self):
        if self.head is None:
            print(termcolor.colored("Linked List is empty!!", "red")) 
        else:
            n = self.tail
            while n is not None:
                print(termcolor.colored(f"{n.data} <== ", "light_blue"), end= " ")
                n = n.pref

    def add_Begain(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.pref = None
            self.head.pref = new_node
            new_node.nref = self.head
            self.head = new_node


    def add_End(self, data):
        if self.head is None:
            print(termcolor.colored("Linked list is empty!! the new node will be added at the begain of the list", "red"))
            dLL1.add_Begain(data)
        else:
            new_node = Node(data)
            n = self.head
            while n.nref is not None:
                n= n.nref
            else:
                n.nref = new_node
                new_node.pref = n
                self.tail = new_node

    def add_before(self, data, x):
        if self.head is None:
            print(termcolor.colored("Linked List is empty!!", "red"))
        else:
            new_node = Node(data)
            n = self.tail 
            while n is not None:
                if n.data == x:
                    new_node.pref = n
                    new_node.nref = n.nref
                    n.nref = new_node
                    previuos_Node.pref = new_node
                    break
                else:
                    previuos_Node = n
                    n = n.pref
                    


    def add_After(self, data, x):
        if self.head is None:
            print(termcolor.colored("Linked List is empty!!", "red"))
        else:
            new_node = Node(data)
            n = self.head 
            while n.nref is not None:
                if n.data == x:
                    new_node.nref = n
                    new_node.pref = n.pref
                    previuos_Node.nref = new_node
                    n.pref = new_node
                    break
                else:
                    previuos_Node = n
                    n = n.nref

    def del_Begian(self):
        if self.head is None:
            print(termcolor.colored("The linked list is empty!!", "red"))
        else:
            n = self.head
            self.head = n.nref
            self.head.pref = None
            n.nref = None
            n.pref = None
            print(termcolor.colored("The first node of the linked list has been deleted sucessfully!!", "light_magenta"))

    def del_End(self):
        if self.head is None:
            print(termcolor.colored("The linked list is empty!!", "red"))
        else:
            n = self.tail.pref
            n.nref = None
            self.tail = n

            print(termcolor.colored("The end node of the linked list has been deleted sucessfully!!", "light_magenta"))


    def del_Node(self, data):
        isDeleted = False
        if self.head is None:
            print(termcolor.colored("Linked list is empty!!", "red"))
        else:
            n = self.head
            while n is not None:
                if n.data == data:
                    n.pref.nref = n.nref
                    n.nref.pref = n.pref
                    n.pref = None
                    n.nref = None
                    print(termcolor.colored("node is deleted sucssessfully!!", "light_magenta"))
                    isDeleted = True
                    break
                else:
                    n = n.nref
        if isDeleted == False:
            print(termcolor.colored("Node not found!!", "red"))
    

    def items_Count(self) -> int:
        if self.head is not None:
            counter = 0
            n = self.head
            while n is not None:
                counter += 1
                n = n.nref
            return counter
        else:
            counter = 0
            return counter
        
    def Check_Empty(self):
        if self.head is None:
            print(termcolor.colored("Linked List is empty!!","light_magenta"))
        else:
            print(termcolor.colored("Linked list is not empty!!", "light_magenta"))

    def clear_list(self):
            if self.head is not None:
                n = self.head
                while n is not None:
                    self.head = n.nref
                    n.nref = None
                    n.pref =None
                    n = self.head
                return True
            else:
                return False



dLL1 = Doubly_Linked_list()

    
while True:
    user_selection = int(input(termcolor.colored("""Please select the action needed 
                               1 => Add node.
                               2 => Delete node.
                               3 => check empty.
                               4 => print list nodes.
                               5 => Linked list Nodes count.
                               6 => Clear Linked List.
                               7 => Print reverse linked list. 
                               8 => Quite The app. \n""", "yellow")))
    
    if user_selection == 1:
            while True:
                second_selection = int(input(termcolor.colored("""Select where you want to add the node
                                1 => Add node at the begaining. 
                                2 => Add node at the end.
                                3 => Add befor specific Node.
                                4 => Add after specific node. 
                                5 => Go to the main menu. \n""", "yellow")))

                if second_selection == 1:
                    data = int(input("Please enter the node data: "))
                    dLL1.add_Begain(data)
                    print("=" * 60)
                    dLL1.print_List()
                    print("\n", end="")
                    print("=" * 60)

                elif second_selection == 2:
                    data = int(input("Please enter the node data: "))
                    dLL1.add_End(data)
                    print("=" * 60)
                    dLL1.print_List()
                    print("\n", end="")
                    print("=" * 60)

                elif second_selection == 3:
                    data = int(input("Please enter the node data: "))
                    x = int(input("Please add the specific node data: "))
                    dLL1.add_before(data, x)
                    print("=" * 60)
                    dLL1.print_List()
                    print("\n", end="")
                    print("=" * 60)

                elif second_selection == 4:
                    data = int(input("Please enter the new node data: "))
                    x = int(input("Please add the specific node data: "))
                    dLL1.add_After(data, x)
                    print("=" * 60)
                    dLL1.print_List()
                    print("\n", end="")
                    print("=" * 60)

                elif second_selection == 5:
                    break

    elif user_selection == 2:
            while True:
                second_selection = int(input(termcolor.colored("""Please select the action needed
                                1 => Delete node at the begaining 
                                2 => Delete node at the end. 
                                3 => Delete Node by value 
                                4 => Go to the main menu \n""", "yellow")))
                
                if second_selection == 1: 
                    dLL1.del_Begian()
                    print("=" * 60)
                    dLL1.print_List()
                    print("\n", end="")
                    print("=" * 60)

                elif second_selection == 2:
                    dLL1.del_End()
                    print("=" * 60)
                    dLL1.print_List()
                    print("\n", end="")
                    print("=" * 60)

                elif second_selection == 3:
                    data = int(input("Pleaser enter the Node value that you want to delete: "))
                    dLL1.del_Node(data)
                    print("=" * 60)
                    dLL1.print_List()
                    print("\n", end="")
                    print("=" * 60)

                elif second_selection == 4:
                    break
    elif user_selection == 3:
        count = dLL1.Check_Empty()
        
    elif user_selection == 4:
        print("=" * 60)
        dLL1.print_List()
        print("\n", end="")
        print("=" * 60)

    elif user_selection == 5:
        counter = dLL1.items_Count()
        if counter is None:
            print("=" * 60)
            print(termcolor.colored("Linked List is Empty!!", "red"))
            print("=" * 60)
        else:
            print("=" * 60)
            print(termcolor.colored(f"linked list items count is {counter}", "light_blue"))
            print("=" * 60)

    elif user_selection == 6:
        isCleared = dLL1.clear_list()
        if isCleared == True:
            print(termcolor.colored("List Cleared Successfully!!", "light_magenta"))
        else:
            print(termcolor.colored("List Already cleared!!", "light_magenta"))
    

    elif user_selection == 7:
        print("=" * 60)
        dLL1.reverse_print_List()
        print("\n", end="")
        print("=" * 60)

    elif user_selection == 8:
        print("=" * 60)
        print(termcolor.colored("Thanks for using my application", "red"))
        print("=" * 60)
        exit()



# This is a full appliction for circuler Linked list.
# this only differance between doubly linked list and circuler linked is is that circuler will have a
# next value at the tail ineasted of None, and have a previous valus at the head insteade of None
# this will cause a infinity loop if we don't pay an attention in loops.

import termcolor
import pyfiglet

print(termcolor.colored(pyfiglet.figlet_format("Circluer Linked list App"),"light_green"))

class Node:
    def __init__(self, data) -> None:
        self.prev = None
        self.data = data
        self.next = None

class circuler_Linked_List():
        def __init__(self) -> None:
            self.head = None
            self.tail = None

        #print Linked list
        def print_list(self):
            if self.head is None:
                print(termcolor.colored("Linked List is empty!!","light_magenta"), end= " ")
            else:
                n = self.head
                flag = True
                while flag:
                    print(termcolor.colored(f"{n.data} ==>", "light_magenta"), end= " ")
                    n = n.next
                    if n == self.tail.next:
                        flag = False

        #print reverse Linked list
        def print_reverse(self):
            if self.head is None:
                print(termcolor.colored("Linked List is empty!!","light_magenta"), end= "")
            else:
                n = self.tail
                flag = True
                while flag:
                    print(termcolor.colored(f"<== {n.data}", "light_magenta"), end= " ")
                    n = n.prev
                    if n == self.head.prev:
                        flag = False

        # print Nodes with Next and Previuos
        def print_Node_Next_Prev(self):
            if self.head is None:
                print(termcolor.colored("Linked List is empty!!","light_magenta"))
            else:
                 n = self.head
                 flag = True
                 while flag:
                      print(termcolor.colored(f"{n.prev.data} <== {n.data} ==> {n.next.data}", "light_magenta"))
                      n = n.next
                      if self.tail.next == n:
                           flag = False

        #count linked list nodes
        def list_len(self):
            counter = 0
            if self.head is None:
                counter = 0
            else:
                 n = self.head
                 flag = True                 
                 while flag:
                      counter += 1
                      n = n.next
                      if self.tail.next == n:
                           flag = False
            return counter
        
        def clear_List(self):
            if self.head is None:
                print(termcolor.colored("Linked List is empty!!","light_magenta"))
            else:
                n = self.head
                flag = True
                while flag:
                      self.head = n.next
                      n.next = None
                      n.prev = None
                      n = self.head

                      if n == self.tail.next:
                           flag = False
                print(termcolor.colored("List cleared sucssessfully!!", "light_magenta"))
                
                      


        # Add node at the begian of the linked list
        def add_begain(self, data):
            new_node = Node(data)
            if self.head is None:
                    self.head = new_node
                    self.head.next = new_node
                    self.head.prev = new_node
                    self.tail = new_node
                    self.tail.next = new_node
                    self.tail.prev = new_node
            else:
                    new_node.prev = self.tail
                    new_node.next = self.head
                    new_node.next.prev = new_node
                    self.head = new_node
                    self.tail.next = new_node

                  
        # Add node at the end of linked list
        def add_End(self, data):
            if self.head is None:
                print(termcolor.colored("Linked list is empty!!", "red"))
            else:
                new_node = Node(data)
                new_node.next = self.head
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
                self.head.prev = new_node

        #Add node at before specific node
        def add_before(self, data, x):
            if self.head is None:
                print(termcolor.colored("Linked list is empty!!", "red"))
            elif x == self.tail.data:
                print(termcolor.colored("This Node is equal to the tail!!, use add to the end option", "red"))
            else:
                 new_node = Node(data)
                 n = self.head
                 while n != self.tail:
                    if x == n.data:
                        n.next.prev = new_node
                        new_node.next = n.next
                        n.next = new_node
                        new_node.prev = n
                        break
                    else:
                         n = n.next
        
        #Add node after specific node
        def add_After(self, data, x):
            if self.head is None:
                print(termcolor.colored("Linked list is empty!!", "red"))
            elif x == self.head.data:
                print(termcolor.colored("This Node is equal to the head!!, use add to the brgian option", "red"))
            else:
                 new_node = Node(data)
                 n = self.tail
                 flag = True
                 while n != self.head:
                      if n.data == x:
                           new_node.prev = n.prev
                           new_node.next = n
                           n.prev.next = new_node
                           n.prev = new_node
                           break
                      else:
                           n = n.prev

        # Delete beain Node
        def del_Begain(self):
            if self.head is None:
                print(termcolor.colored("Linked list is empty!!", "red"))
            else:
                if self.head != self.tail:
                    n = self.head.next
                    n.prev = self.head.prev
                    self.head.next = None
                    self.head.prev = None
                    self.head = n
                    self.tail.next = n
                else:
                     self.head = None
                     self.tail = None
        
        #delete end node
        def del_End(self):
            if self.head is None:
                print(termcolor.colored("Linked list is empty!!", "red"))
            else:
                if self.head != self.tail:
                      n = self.tail.prev
                      n.next = self.tail.next
                      self.tail.next = None
                      self.tail.prev = None
                      self.tail = n
                      self.head.prev = n
                else:
                    self.head = None
                    self.tail= None

        #delete node
        def del_Node(self, x):
            if self.head is None:
                print(termcolor.colored("Linked list is empty!!", "red"))

            elif x == self.head.data:
                 cLL1.del_Begain()
            elif x == self.tail.data:
                 cLL1.del_End()
            else:
                 n = self.head
                 print(type(n.data))
                 flag = True
                 while flag:
                      if n.data == x:
                           n.next.prev = n.prev
                           n.prev.next = n.next
                           n.next = None
                           n.prev = None
                           break
                      else:
                           n = n.next

                 





                           
                        



                      
            



                


cLL1 = circuler_Linked_List()

# Determin user selection
while True:
    user_selection = int(input(termcolor.colored("""Please select the action needed 
                        1 => Add node.
                        2 => Delete node.
                        3 => check empty.
                        4 => print list nodes.
                        5 => Print reverse linked list.
                        6 => print each node with next and prev.
                        7 => Linked list Nodes count.
                        8 => Clear Linked List.
                        9 => Get head and tail. 
                        10 => Quite The app. \n""", "yellow")))
    # Adding New node
    if user_selection == 1:
           while True:
                second_selection = int(input(termcolor.colored("""Select where you want to add the node
                                1 => Add node at the begaining. 
                                2 => Add node at the end.
                                3 => Add befor specific Node.
                                4 => Add after specific node. 
                                5 => Go to the main menu. \n""", "light_cyan")))
                
                if second_selection == 1:
                    data = input("Please enter the value of the node: ")
                    cLL1.add_begain(data)
                    print("=" * 60)
                    cLL1.print_list()
                    print("\n", end="")
                    print("=" * 60)

                elif second_selection == 2:
                    data = input("Please enter the value of the node: ")
                    cLL1.add_End(data)
                    print("=" * 60)
                    cLL1.print_list()
                    print("\n", end="")
                    print("=" * 60)

                elif second_selection == 3:
                    data = input("Please enter the value of the node: ")
                    x = input("please input the node value that you want to add before")
                    cLL1.add_before(data, x)
                    print("=" * 60)
                    cLL1.print_list()
                    print("\n", end="")
                    print("=" * 60)
                elif second_selection == 4:
                    data = input("Please enter the value of the node: ")
                    x = input("please input the node value that you want to add After")
                    cLL1.add_After(data, x)
                    print("=" * 60)
                    cLL1.print_list()
                    print("\n", end="")
                    print("=" * 60)

                elif second_selection == 5:
                     break




    # Delete Node
    elif user_selection == 2:
            while True:
                second_selection = int(input(termcolor.colored("""Please select the action needed
                                1 => Delete node at the begaining 
                                2 => Delete node at the end. 
                                3 => Delete Node by value 
                                4 => Go to the main menu \n""", "light_cyan")))
                
                # Delete First Node
                if second_selection == 1:
                    cLL1.del_Begain()
                    print("=" * 60)
                    cLL1.print_list()
                    print("\n", end="")
                    print("=" * 60)

                # Delete End Node
                elif second_selection == 2:
                    cLL1.del_End()
                    print("=" * 60)
                    cLL1.print_list()
                    print("\n", end="")
                    print("=" * 60)

                # Delete specific Node
                elif second_selection == 3:
                        x = input("Please enter the node data")
                        cLL1.del_Node(x)
                        print("=" * 60)
                        cLL1.print_list()
                        print("\n", end="")
                        print("=" * 60)

                elif second_selection == 4:
                     break
                
    elif user_selection == 3:
        if cLL1.head is None:
            print("=" * 60)
            print(termcolor.colored("linked list is empty", "light_magenta"))
            print("=" * 60)
        else:
            print("=" * 60)
            print(termcolor.colored("Linked list is not empty!!", "light_magenta"))
            print("=" * 60)

    elif user_selection == 4:
            print("=" * 60)
            cLL1.print_list()
            print("\n", end="")
            print("=" * 60)

    elif user_selection == 5:
            print("=" * 60)
            cLL1.print_reverse()
            print("\n", end="")
            print("=" * 60)

    elif user_selection == 6:
         print("=" * 60)
         cLL1.print_Node_Next_Prev()
         print("=" * 60)
    
    elif user_selection == 7:
        count = cLL1.list_len()
        if count == 0:
            print("=" * 60)
            print(termcolor.colored("linked list is empty", "light_magenta"))
            print("=" * 60)
        else:
            print("=" * 60)
            print(termcolor.colored(f"linked list nodes count is {count}", "light_magenta"))
            print("=" * 60)

    elif user_selection == 8:
         
        print("=" * 60)
        cLL1.clear_List()
        print("=" * 60)

    elif user_selection == 9:
        if cLL1.head is None:
            print("=" * 60)
            print(termcolor.colored("linked list is not empty", "light_magenta"))
            print("=" * 60)
        else:
            print("=" * 60)
            print(termcolor.colored(f"list Head is {cLL1.head.data} and tail is {cLL1.tail.data}", "light_magenta"))
            print("=" * 60)

    elif user_selection == 10:
        print("=" * 60)
        print(termcolor.colored("Thanks for using my app", "light_magenta"))
        print("=" * 60)
        exit()
        

         

                     



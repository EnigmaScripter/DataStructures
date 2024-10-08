# Stacks ould be implemented in python through list and modules.
# stacks have 4 main operations which are:
#       1- Push => Adding element to the stack.
#       2- pop => removing element to the stack.
#       2- Isempty => check if the stack is empty.
#       2- ontop element => check the on top element of a stack.

# we can use 
# list.append() as a push method and 
# list.pop() as a pop method
# len(list) as isempty method or not key word and 
# -1 index to access the last added element 

stack = []

stack.append(3) # Adding one by one elememt
stack.append(4)
stack.append(5)

print(stack)

print(stack.pop()) # pop will return the element value that has been removed

print(len(stack) == 0) # it will return False as the stack is not empty.

print(not stack) # it will also return false as the stack is not empty.

print(stack[-1]) # will retrun 4 as it is the last added element to the stack


# This is a full implementation for stack data structure on python
stack= [] # creating the stack
def stack_Push(element): #push
    stack.append(element)
    print(sorted(stack))
 
def stack_pop(): # pop
    if not stack:
        print("stack is empty")
    else:
        stack.pop()
        print(sorted(stack))

def stack_Empty(): # id empty
    print(not stack)
    pass

def stack_Ontop_Element(): #got the ontop element
    if not stack:
        print("The top element is index 0")
    else:
        print(f"the top element is {stack[-1]}")

while True:
    userSelection = int(input("Please select the operation you want(1 => push, 2 => pop, 3 => check empty 4 => find the last element) "))
    if userSelection == 1:
        element= input("please enter the element: ")
        stack_Push(element)
    elif userSelection == 2:
        stack_pop()
    elif userSelection == 3:
        stack_Empty()
    elif userSelection == 4:
        stack_Ontop_Element()










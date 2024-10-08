"""Queue is a user defined data structure that support liner data""" 
""" we could use collections deque class """

import collections

""" COllection double end queue is a class that accept adding or removing items form both sides of the queue
So, if we will add item to the right side of the queue we will use append method 'queue.append()' and to remove
an item from the queue from the left side we could use the method popleft 'queue.popleft() and vice versa"""




# a full program to implement queue through built in list

queue = collections.deque()

queue.append(3) # Adding one by one elememt to the right side of the queue
queue.append(4)
queue.append(5)

print(queue)

print(queue.popleft()) # popleft() will return the first inserted element at the right side of the queue that has been removed

print(len(queue) == 0) # it will return False as the queue is not empty.

print(not queue) # it will also return false as the queue is not empty.

print(queue[-1]) # will retrun 4 as it is the last added element to the queue
print(queue[0]) # will return 3 as it is the first element will be remobed from the queue.


# This is a full implementation for queue data structure on python
queue= collections.deque() # creating the double ended queue
def queue_Push(element): #push
    queue.append(element)
    print(queue)
 
def queue_pop(): # pop
    if not queue:
        print("queue is empty")
    else:
        queue.popleft() # this will be wrong if the list is sorted!!!!
        print(queue)

def queue_Empty(): # id empty
    print(not queue)

def queue_Ontop_Element(): #got the ontop element
    if not queue:
        print("The top element is index 0")
    else:
        print(f"the top element is {queue[0]}")

def extend_queus(list):
    queue.extend(list)

while True:
    userSelection = int(input("Please select the operation you want(1 => push, 2 => pop, 3 => check empty 4 => find the last element) "))
    if userSelection == 1:
        element= int(input("please enter the element: "))
        queue_Push(element)
    elif userSelection == 2:
        queue_pop()
    elif userSelection == 3:
        queue_Empty()
    elif userSelection == 4:
        queue_Ontop_Element()
    elif userSelection == 5:
        element= set(map(int, input("please enter a list of elements : ").split()))
        print(element)
        extend_queus(element)
    else:
        break
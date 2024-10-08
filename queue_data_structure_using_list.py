"""Queue is a user defined data structure that support liner data 
verses queues, queue is using First in Firest out method to append and remove elements from the 
queue which data inserted in one side and removed in the other side """

# a full program to implement queue through built in list

queue = []

queue.append(3) # Adding one by one elememt
queue.append(4)
queue.append(5)

print(queue)

print(queue.pop(0)) # pop(0) will return the first inserted element value that has been removed

print(len(queue) == 0) # it will return False as the queue is not empty.

print(not queue) # it will also return false as the queue is not empty.

print(queue[-1]) # will retrun 4 as it is the last added element to the queue
print(queue[0]) # will return 3 as it is the first element will be remobed from the queue.


# This is a full implementation for queue data structure on python
queue= [] # creating the queue
def queue_Push(element): #push
    queue.append(element)
    print(queue)
 
def queue_pop(): # pop
    if not queue:
        print("queue is empty")
    else:
        queue.pop(0) # this will be wrong if the list is sorted!!!!
        print(queue)

def queue_Empty(): # id empty
    print(not queue)

def queue_Ontop_Element(): #got the ontop element
    if not queue:
        print("The top element is index 0")
    else:
        print(f"the top element is {queue[0]}")

while True:
    userSelection = int(input("Please select the operation you want(1 => push, 2 => pop, 3 => check empty 4 => find the last element) "))
    if userSelection == 1:
        element= input("please enter the element: ")
        queue_Push(element)
    elif userSelection == 2:
        queue_pop()
    elif userSelection == 3:
        queue_Empty()
    elif userSelection == 4:
        queue_Ontop_Element()
    else:
        break


# 
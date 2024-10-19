"""priority queue is a queue that remove the elements by it priority."""

import queue

q = queue.PriorityQueue()

q.put(10)
q.put(20)
q.put(30) 
q.put(40)
print(q)

print(q.pop(0))


while not q.empty():
    print(q.get())
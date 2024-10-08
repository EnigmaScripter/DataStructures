# stack using different modules

#using collection modules
import collections

stack = collections.deque()
print(sorted(stack))

stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(15)

print(sorted(stack))

stack.pop()
print(stack)

#using queue module

import queue
stack = queue.LifoQueue()
print(stack)

stack.put(10)
stack.put(20)
stack.put(15)
stack.put(40)


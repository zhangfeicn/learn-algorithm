"""
Deque is preferred over list in the cases where we need quicker append and pop
operations from both the ends of the container, as deque provides an O(1)
time complexity for append and pop operations as compared to list which
provides O(n) time complexity.

deque can be handled in python by module named "collections".
    append(x) - add x to the right side.
    appendleft(x) - add x to the left side
    pop() - pop from the right side
    popleft() - pop from the left side
"""

from collections import deque

_created = "2020-04-02"

dequeue = deque()
for i in range(10):
    dequeue.append(i)

# operate on the queue
print("De-Queue Operations:\n")
print("Initial de-queue: " + str(dequeue))
print("popleft(): " + str(dequeue.popleft()))
print("pop(): " + str(dequeue.pop()))
print(
    "After popleft() and pop(), the de-queue is now: ",
    str(dequeue))
print("first - deque[0]: " + str(dequeue[0]))
print("last - deque[-1]: " + str(dequeue[-1]))
dequeue.appendleft(0)
print("After appendleft(0), the de-queue is now: " + str(dequeue))
dequeue.append(9)
print("After append(9), the de-queue is now: " + str(dequeue))
print("size(): " + str(len(dequeue)))

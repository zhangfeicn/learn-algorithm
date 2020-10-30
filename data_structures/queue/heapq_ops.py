"""
heapq - Heap queue algorithm (a.k.a. priority queue)

Heaps are arrays for which a[k] <= a[2*k+1] and a[k] <= a[2*k+2] for
all k, counting elements from 0.
    heapify(L) - transform list into a heap
    nlargest(k, iterable) - Produce a list of the k largest values from a
        given iterable
    nsmallest(k, iterable) - Produce a list of the k smallest values from a
        given iterable
    heappop(L) - pop the smallest item off the heap
    heappush(L, e) - Push element e onto list L and restore the heap-order
        property
    heappushpop(L, e) - Push element e on list L and then pop and return the
        smallest item.
    heapreplace(L, e) - Similar to heappushpop, but equivalent to the pop being
        performed before the push
"""

import heapq

_created = "2020-05-07"

nums = [1, 5, 90, 67, 35, 15, 70]
heap = []

print('Method 1 - using heappush:')
for num in nums:
    heapq.heappush(heap, num)
print(heap)
print('Smallest in the heap:', heap[0])
print('Heap sort results:', end='')
print([heapq.heappop(heap) for _ in range(len(nums))])

print('Method 2 - using heapify:')
heapq.heapify(nums)
print(nums)
print('Smallest in the heap:', nums[0])
print('Heap sort results:', end='')
print([heapq.heappop(nums) for _ in range(len(nums))])

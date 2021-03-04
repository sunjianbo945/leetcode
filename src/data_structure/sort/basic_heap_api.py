from heapq import *

heap = []  # the heap declared as list, use library heapq to offer and poll
for i in reversed(range(5)):
    heappush(heap, i)  # add element into heap, O(logn)

print(f"min heap by default: {heap}")

heap_copy = list(heap)
while heap_copy:
    print(f"heap pop() : {heappop(heap_copy)}")  # O(logn)

print(f'peek the top element in the heap: {heap[0]}')
print(f'heap is empty? {not heap}')
print(f'heap size is {len(heap)}')

arr = []
for i in reversed(range(5)):
    arr.append(i)

print(f'list is {arr}')
heapify(arr)
print(f'after heapify(): {arr}')

maxHeap = []

for i in range(5):
    heappush(maxHeap, (-i))

print(f'max heap use negative number: {maxHeap}')

stringMaxHeap = []


class Node:
    def __init__(self, string):
        self.string = string

    def __lt__(self, other):
        return other.string < self.string  # the source code use newItem < exist to compare

    # The __str__ is for end users. The essential purpose is to explain what data the object contains in a readable manner.
    # simple print object will use str
    def __str__(self):
        print('__str__')
        return self.string

    # The __repr__ is for developers. The essential purpose is to explain what the object is in an unambiguous way.
    # list object print will use repr
    # used on the console
    def __repr__(self):
        print('__repr__')
        return self.string


for i in range(5):
    heappush(stringMaxHeap, Node(chr(ord('a') + i)))

print(f'max heap for string: {stringMaxHeap}')
print(f'peek the top element : {stringMaxHeap[0]}')

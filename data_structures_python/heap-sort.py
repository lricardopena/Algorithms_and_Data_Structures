
import numpy as np
import math as mt


heap_size = 0

def partent(i):
    return mt.floor((i+1)/2.) - 1

def left(i):
    return 2*(i+1) - 1

def right(i):
    return 2*(i+1)

def update_heap_size(A):
    global heap_size
    heap_size = -1
    for i in range(1,len(A)):
        if A[partent(i)] < A[i]:
            heap_size = i - 1
            break

def max_heapify(A,i):
    l = left(i)
    r = right(i)
    largest = 0
    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r < heap_size and A[r] > A[largest]:
        largest = r

    if largest != i:
        Ai = A[i]
        Alargest = A[largest]
        A[i] = Alargest
        A[largest] = Ai
        #update_heap_size(A)
        max_heapify(A, largest)

def build_max_heap(A):
    global heap_size
    heap_size = len(A)
    for i in range(int(mt.floor(len(A)/2)),-1,-1):
        max_heapify(A,i)




A = np.array(np.random.randint(1,100,size=20))

build_max_heap(A)


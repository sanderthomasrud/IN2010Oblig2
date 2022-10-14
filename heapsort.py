import math
from matplotlib import mathtext

def sort(A):
    n = len(A)
    MaxHeap(A, n)
    for i in range(n-1, -1, -1):
        A[0], A[i] = A[i], A[0]
        MaxHeapHelp(A, 0, i)
        
    return A
    # Do insertion sort here. Use the Sorter's comparison- and swap
    # methods for automatically counting the swaps and comparisons.

    # Use A.swap(i, j) to swap the values at two indices i and j. The swap is
    # counted, when using this method. Comparisons are counted automatically.


# heap A, rot i, n elements
def MaxHeapHelp(A, i, n):
    largest = i
    left = 2*i+1
    right = 2*i+2

    if left < n and A[largest] < A[left]:
        largest, left = left, largest

    if right < n and A[largest] < A[right]:
        largest, right = right, largest

    if i != largest:
        # A[i], A[largest] = A[largest], A[i]
        A.swap(i, largest)
        MaxHeapHelp(A, largest, n)

# array A, N elements
def MaxHeap(A, n):
    for i in range(math.floor(n/2), -1, -1):
        MaxHeapHelp(A, i, n)


import math
import countswaps

def sort(A):
    low = 0
    high = len(A) - 1

    A = Quicksort(A, low, high)
    # Do quicksort here. Use the Sorter's comparison- and swap
    # methods for automatically counting the swaps and comparisons.

    # Use A.swap(i, j) to swap the values at two indices i and j. The swap is
    # counted, when using this method. Comparisons are counted automatically.

    return A

def Quicksort (A, low, high):
    if low >= high:
        return A
    
    p = Partition(A, low, high)
    Quicksort(A,low,p-1)
    Quicksort(A, p+1, high)
    return A

def Partition(A, low, high):
    p = Choosepivot(A, low, high)
    A[p], A[high] = A[high], A[p]


    pivot = A[high]
    left = low
    right = high - 1

    while left <= right:
        while left <= right and A[left] <= pivot:
            left = left + 1
            
        while right >= left and A[right] >= pivot:
            right = right - 1
            
        
        if left < right:
            A[left], A[right] = A[right], A[left]
            # A.swap(left, right)
      


    # A[left], A[high] = A[high], A[left]
    A.swap(left, right)
    return left

def Choosepivot(A, low, high):
    median = math.floor((low + high) / 2)

    return median
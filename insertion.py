import countswaps

def sort(A):
    for i in range(len(A)):
        j = i
        while j > 0 and A[j-1] > A[j]:
            # A[j-1], A[j] = A[j],A[j-1]
            A.swap(j-1, j)

            j = j-1
    # Do insertion sort here. Use the Sorter's comparison- and swap
    # methods for automatically counting the swaps and comparisons.

    # Use A.swap(i, j) to swap the values at two indices i and j. The swap is
    # counted, when using this method. Comparisons are counted automatically.

    return A

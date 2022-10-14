
def sort(A):
    for i in range(len(A) - 1):
        for j in range(len(A) - i - 1):
            if A[j] > A[j+1]:
                # A[j], A[j+1] = A[j+1], A[j]
                A.swap(j, j+1)
    # Do insertion sort here. Use the Sorter's comparison- and swap
    # methods for automatically counting the swaps and comparisons.

    # Use A.swap(i, j) to swap the values at two indices i and j. The swap is
    # counted, when using this method. Comparisons are counted automatically.

    return A
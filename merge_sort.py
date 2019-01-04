def merge(arr, l, m, r):
    """
    Merges the two sorted list

    """

    L = arr[l:m+1]
    R = arr[m+1:r+1]

    n1 = len(L)
    n2 = len(R)

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:

        if L[i] < R[j]:

            arr[k] = L[i]
            i += 1
        
        else:

            arr[k] = R[j]
            j += 1

        k +=1

    while i < n1:

        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:

        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, l, r):
    """
    Implementation of Merge sort Algorithm.

    """

    if l < r:

        m = l + (r-l) // 2

        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l, m, r)
    
    else:
        pass



arr = [9, 8, 2, 7, 8, 4, 6, 4]

merge_sort(arr, 0, 7)
print(arr)

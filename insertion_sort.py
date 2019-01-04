def insertion_sort(arr):
    """
    Implemetation of Insertion sort Algorithm.

    """

    num = 0
    n = len(arr)

    for i in range(1, n):

        num = arr[i]
        j = i

        while num < arr[j - 1] and j > 0:

            j -= 1

        else:

            arr.insert(j, num)
            arr.pop(i + 1)
    
    return arr


arr = [2, 9, 4, 1, 6, 5, 3]
print(insertion_sort(arr))

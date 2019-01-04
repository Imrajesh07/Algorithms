def bubble_sort(arr):
    """
    Implementation of Bubble sort algorithm.

    """

    n = len(arr)

    for i in range(n-1):

        for j in range(n-i-1):

            if arr[j+1] < arr[j]:

                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return(arr)

arr = [2, 3, 4, 7, 6, 9, 11]
print(bubble_sort(arr))

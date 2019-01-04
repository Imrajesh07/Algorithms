def selection_sort(arr):
    """
    Implementation of Selection sort Algorithm

    """

    sorted_arr = []
    n = len(arr)

    for i in range(n):
        min_num = arr[0]
        
        for j in range(1, len(arr)):

            if arr[j] < min_num:
                min_num = arr[j]
        
        sorted_arr.append(min_num)
        arr.remove(min_num)
    
    return sorted_arr


arr = [1, 3, 2, 4, 10, 4, 7, 9]

print(selection_sort(arr))

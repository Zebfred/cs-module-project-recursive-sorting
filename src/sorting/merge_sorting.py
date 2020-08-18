# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    x = 0 
    y = 0

    # Your code here
    for i in range(0, elements):
        if x == len(arrA):
            merged_arr[i] = arrB[y]
            y += 1

        elif y == len(arrB):
            merged_arr[i] = arrA[x]
            x += 1

        elif arrA[x] < arrB[y]:
            merged_arr[i] = arrA[x]
            x += 1  

        elif arrA[x] > arrB[y]:
            merged_arr[i] = arrB[y]
            y += 1         

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        arrA = arr[:middle]
        arrB = arr[middle:]
        arrA = merge_sort(arrA)
        arrB = merge_sort(arrB)
        return merge(arrA, arrB)
    # Your code here


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass


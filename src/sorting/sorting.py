import math

# TO-DO: complete the helper function below to merge 2 sorted arrays


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    countA = 0
    countB = 0

    for i in range(0, elements):
        if countA == len(arrA):
            merged_arr[i] = arrB[countB]
            countB += 1
        elif countB == len(arrB):
            merged_arr[i] = arrA[countA]
            countA += 1
        elif arrA[countA] < arrB[countB]:
            merged_arr[i] = arrA[countA]
            countA += 1
        elif arrA[countA] > arrB[countB]:
            merged_arr[i] = arrB[countB]
            countB += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        mid = math.floor(len(arr)/2)
        a = arr[0:mid]
        b = arr[mid:]
        arr = merge(merge_sort(a), merge_sort(b))

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    return arr

def merge_sort_in_place(arr, l, r):
    # Your code here
    return arr
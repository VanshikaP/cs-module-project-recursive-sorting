# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    i, j = 0,0
    k = 0

    # comparing and replacing elements in merged_arr till minimum of len(arrA) and len(arrB)
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            i += 1
        else:
            merged_arr[k] = arrB[j]
            j += 1
        k += 1

    # copying remaining elements from A to merged_arr
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i += 1
        k += 1
    
    # copying remaining elements from B to merged_arr
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        j += 1
        k += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) < 2:
        return arr
    else:
        mid = len(arr)// 2
        part1 = merge_sort(arr[0:mid])
        part2 = merge_sort(arr[mid:])
        return merge(part1, part2)

print(merge([0,1], [2,3,5]))

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


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



# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    start2 = mid
    while start <= mid and start2 <= end:
        if arr[start] <= arr[start2]:
            start += 1
        else:
            index = start2
            value = arr[start2]
            while index is not start:
                arr[index] = arr[index - 1]
                index -= 1
            arr[start] = value
            start += 1
            mid += 1
            start2 += 1
    return arr

print(merge_in_place([1,5,8,2,4], 0, 2, 4))
def merge_sort_in_place(arr, l, r):
    # Your code here
    if r - l < 1:
        return arr
    else:
        m = (l + r) // 2
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)
        return merge_in_place(arr, l, m+1, r)


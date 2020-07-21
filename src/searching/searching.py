# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if len(arr) is 0:
        return -1
    if start is end:
        if target is arr[start]:
            return start
        else:
            return -1
    else:
        mid = (start + end) // 2
        if target is arr[mid]:
            return mid
        elif target < arr[mid]:
            return binary_search(arr, target, start, mid - 1)
        else:
            return binary_search(arr, target, mid + 1, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    if len(arr) is 0:
        return -1
    if len(arr) is 1:
        if target is arr[0]:
            return 0
        else:
            return -1
    
    order = 1
    if arr[1] < arr[0]:
        order = -1
    
    mid = len(arr) // 2
    if target is arr[mid]:
        return mid
    elif (target < arr[mid] and order is 1) or (target >arr[mid] and order is -1):
        return agnostic_binary_search(arr[0:mid], target)
    elif (target < arr[mid] and order is -1) or (target > arr[mid] and order is 1):
        index = agnostic_binary_search(arr[mid+1:], target)
        if index is -1:
            return -1
        else:
            return mid + index + 1


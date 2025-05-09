def binary_search(arr, target):
    left , right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2 
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1

sorted_arr = [1,2,3,4,5,6,12,14,21,30]
x = binary_search(sorted_arr, 14)
print(f'The target is at index: {x}')
'''
input: 
arr = [2,4,5,5,5,5,5,7,9,9]
target = 5 
output: [2, 6]

'''

def first_and_last(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            start = i

            while (i + 1 < len(arr)) and arr[i+1] == target:
                i += 1
                last = i
            return [start, last]
        
    return [-1, -1]

assert [2, 6] == first_and_last([2,4,5,5,5,5,5,7,9,9], 5) # True
assert [8, 9] == first_and_last([2,4,5,5,5,5,5,7,9,9], 9) # True


def find_start(arr, target):
    if arr[0] == target:
        return 0
    
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target and arr[mid - 1] < target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1 

def find_end(arr, target):

    if arr[-1] == target:
        return len(arr) - 1

    left, right = 0, len(arr)  - 1
    while left <= right:
        mid = (left + right) // 2 

        if arr[mid] == target and arr[mid + 1] > target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def first_and_last_v2(arr, target):
    
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
        return [-1, 1]

    return [(find_start(arr, target)), find_end(arr, target)]

print(find_start([2,4,5,5,5,5,5,7,9,9], 5))

print(find_end([2,4,5,5,5,5,5,7,9,9], 5))

assert [2, 6] == first_and_last_v2([2,4,5,5,5,5,5,7,9,9], 5) # True
assert [8, 9] == first_and_last_v2([2,4,5,5,5,5,5,7,9,9], 9) # True

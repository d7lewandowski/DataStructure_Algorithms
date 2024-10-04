'''
input: 
arr = [4,2,9,7,5,6,7,1,3]
k = 4
output: 6

1st largest - 9
2nd largest - 7
3rd largest - 7
4th largest - 6
'''


def kth_largest(arr, k):
    for i in range(k - 1):
        arr.remove(max(arr))
    return max(arr)

assert 6 == (kth_largest([4,2,9,7,5,6,7,1,3], 4))

# [1, 2, 3, 4, 5, 6, 7, 7, 9] 4 
def kth_largest_v1(arr, k):
    n = len(arr)
    arr.sort()
    # print(arr)
    return arr[n - k]

kth_largest_v1([4,2,9,7,5,6,7,1,3], 4)
assert 6 == (kth_largest_v1([4,2,9,7,5,6,7,1,3], 4))



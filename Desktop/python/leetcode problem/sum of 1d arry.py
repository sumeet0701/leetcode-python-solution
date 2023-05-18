'''
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
'''

'''
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
'''

## solution:


def array(arr):
    for i in range(1,len(arr)):
        arr[i] = arr[i] + arr[i-1]
    return arr

arr = [1,2,3,4,5,6]
array(arr)
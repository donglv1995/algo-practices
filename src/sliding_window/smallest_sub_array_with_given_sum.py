"""
[Level - Easy]
Problem: Given an array of positive numbers and a positive number 'S', find the length of the smallest contigous subarray whose sum is greater than or equal to 'S'/
Return 0 if no such subarray exists.

Input:
    Array: [2, 1, 5, 2, 3, 2]
    S: 7
Output: 2
Explanation: The smallest subarray with a sum greater than or eqaul to '7' is  [5, 2]

Input: 
    Array: [2, 1, 5, 2, 8]
    S: 7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8]

Input: 
    Array: [3, 4, 1, 1, 6]
    S: 8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6]
"""
def find_min_sub_array(arr, s: int):
    w_sum = 0
    result, sub_array = [], []
    w_start = 0 
    w_end = 1

    for x in arr:
        sub_array = arr[w_start:w_end]
        w_sum = sum(sub_array)

        while w_sum >= s:
            result = sub_array.copy()
            w_sum -= arr[w_start]
            w_start += 1
            sub_array = arr[w_start:w_end]
        
        w_end += 1

    return result

# 2 - [5, 2]
print(find_min_sub_array([2, 1, 5, 2, 3, 2], 7))

# 1 - [8]
print(find_min_sub_array([2, 1, 5, 2, 8], 7))

# 3 - [3, 4, 1] or [1, 1, 6]
print(find_min_sub_array([3, 4, 1, 1, 6], 8))
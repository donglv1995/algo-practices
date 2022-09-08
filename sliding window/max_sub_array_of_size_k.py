"""
[Level - Easy]
Problem: Given an array of positive numbers and a positive number 'k', find the maximum sum of any contigous subarray of size 'k'

Input:
    Array: [2, 1, 5, 1, 3, 2]
    K: 3
Ouput: 9
Explanation: Subarray with maximum sum is [5, 1, 3]

Input:
    Array: [2, 3, 4, 1, 5]
    K: 2
Output: 7
Explanation: Subarray with maximum sum is [3, 4]
"""
def max_sub_array_of_size_k(arr, k: int):
    max_sum, arr_sum = 0, 0
    result, sub_arr = [], []
    w_end = 0, 0

    for x in arr:
        sub_arr.append(x)

        if w_end >= k -1:
            arr_sum = sum(sub_arr)
            
            if arr_sum > max_sum:
                max_sum = arr_sum
                result = sub_arr.copy()

            sub_arr.pop(0)
        
        w_end += 1

    return result

# [5, 1, 3]
print(max_sub_array_of_size_k([2, 1, 5, 1, 3, 2], 3))

# [3, 4]
print(max_sub_array_of_size_k([2, 3, 4, 1, 5], 2))

"""
[Level: Easy]
Problem: Given an array of sorted number and a target sum, find a pair in the array whose sum is equal to the given target.
Write a function to return the indices of the two numbers (i.e the pair) such that they add up to the given target.

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: the nubers at index 1 and 3 add up to 6: 2 + 4 = 6
"""

def pair_with_target_sum(arr, target: int):
    f_pointer = 0
    s_pointer = len(arr) -1
    result = []

    for i in range(0, len(arr) -1):
        array_sum = arr[f_pointer] + arr[s_pointer]
        
        if array_sum == target:
            result.append([f_pointer, s_pointer])
        
        if array_sum > target:
            s_pointer -= 1
        else:
            f_pointer += 1
    
    return result

# [1, 3]
print(pair_with_target_sum([1, 2, 3, 4, 6], 6))

def pair_with_target_sum_hashmap(arr, target: int):
    dict = {}
    result = []

    for i in range(0, len(arr) -1):
        if (dict.__contains__(target - arr[i])):
            result.append([dict.get(target - arr[i]), i])
        else:
            dict[arr[i]] = i
    return result

# [1, 3]
print(pair_with_target_sum_hashmap([1, 2, 3, 4, 6], 6))

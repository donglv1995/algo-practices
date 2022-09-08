"""
[Level: Easy]
Problem: Given an array of sorted numbers, remove all duplicates from it. You SHOULD NOT USE any extra space; after removing the duplicates
in-place the length of the subarray that has no duplicate in it.

Input: [2, 3, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9]

Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11]
"""

def remove_duplicate(arr):
    current_pointer = 1
    count = 1

    for i, val in enumerate(arr):
        if (arr[current_pointer -1] != val):
            arr[current_pointer] = val
            current_pointer += 1
            count += 1
  
    return count

# 4 - [2, 3, 6, 9]
print(remove_duplicate([2, 3, 3, 3, 3, 6, 9, 9]))

# 2 - [2, 11]
print(remove_duplicate([2, 2, 2, 11]))
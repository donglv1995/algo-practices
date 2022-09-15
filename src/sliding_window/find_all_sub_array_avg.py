"""
[Level - Easy]
Problem: Given an array, find the average of all contigous subarrays of size 'K' in it.

Input: 
    Array: [1, 3, 2, 6, -1, 4, 1, 8, 2]
    K: 5

Output: [2.2, 2.8, 2.4, 3.6, 2.8]
---
Solution approach:
    - Sum first K elements as Result
    - Minus first element from Result then Add next elements to Result
"""
def find_avg(arr, k: int):
    result = []
    w_sum = 0.0
    w_start, w_end = 0, 0

    for x in arr:
        w_sum += x

        if (w_end >= k - 1):
            result.append(w_sum / k)
            w_sum -= arr[w_start]
            w_start += 1
        
        w_end += 1
    return result

print(find_avg([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))

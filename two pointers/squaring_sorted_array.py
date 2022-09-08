"""
[Level: Easy]
Problems: Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]

Input: [-3, -1, 0, 1, 2]
Output: [0, 1, 1, 4, 9]

Idea: 
    - Two pointers : one start from beginig of array, one end of array
    - Get the values and squares it
    - Compare both values to each others, higher value should store at the end of result array
    - Move the pointer from higher value site
    - Repeat

"""
def squaring_sorted_array(arr):
    n = len(arr)
    result = [0] * n
    l_pointer = 0
    r_pointer = len(arr) -1
    highest_index = n -1

    while l_pointer <= r_pointer:
        left_square = arr[l_pointer] * arr[l_pointer]
        right_square = arr[r_pointer] * arr[r_pointer]

        if (left_square > right_square):
            result[highest_index] = left_square
            l_pointer += 1
        else:
            result[highest_index] = right_square
            r_pointer -= 1

        highest_index -=1
    return result

# [0, 1, 4, 4, 9]
print(squaring_sorted_array([-2, -1, 0, 2, 3]))

# [0, 1, 1, 4, 9]
print(squaring_sorted_array([-3, -1, 0, 1, 2]))

"""
[Level - Medium]
Problem: Given a string, find the length of the longst substring in it with no more than K distinct characters.
You can assum that K is less than or equal to the length of the given string.

Input: String="araaci", K=2
Ouput: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' characters is "aa".

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
"""

def longest_substring_with_k_distinct():
    return
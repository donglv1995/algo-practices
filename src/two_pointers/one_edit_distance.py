"""
[Level: Easy]
Problem: Given two string s and t, return True if they are both one edit distance apart, otherwise return False

A string s is said to be one edit distance apart from a string t if you can:
    - Insert exactly one character into s to get t
    - Delete exactly one character from s to get t
    - Replace exactly one character of s with a different character to get t.

Input: s="ab", t = "acb"
Output: True
Explanation: We can insert 'c' into s to get t.

Input: s="", t=""
Output: False
Explanation: We cannot get t from s by only on step.
"""
def one_edit_distance(s, t):

    # If length of two strings differ is more than 1 char, so two strings cannot be on edit distance apart 
    if abs(len(s) - len(t)) > 1:
        return False
    
    i = j = edit = 0
    while i < len(s) and j < len(t):
        # match
        if s[i] == t[j]:
            i, j = i + 1, j + 1 # Chars match, move to next char
            continue

        # mismatch
        edit += 1
        if edit > 1:
            return False # diff is more than 1, return False
        
        if len(s) == len(t):
            i, j = i + 1, j + 1
        else:
            if len(s) > len(t):
                i += 1 # delete char form s
            else:
                j += 1 # add char to s

    # any left over chars will have to be delete    
    if i < len(s) or j < len(t):
        edit += 1

    return edit == 1

print(one_edit_distance("ab", "acb"))

print(one_edit_distance("abcdee", "abcee"))

print(one_edit_distance("", ""))

print(one_edit_distance("acb","ecb"))
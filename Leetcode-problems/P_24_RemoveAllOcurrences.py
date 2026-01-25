'''
This is an classical problem on strings for dsa 
Leet Code 1910

Given two strings s and part, perform the following operation 
on s until all occurrences of the substring part are removed:

Find the leftmost occurrence of the substring part and remove it 
from s.
Return s after removing all occurrences of part.

A substring is a contiguous sequence of characters in a string.
'''

def removeOccurrences(s,part) -> str:
    k = len(part)
    while True:
        idx = s.find(part)
        if idx == -1:
            break
        s = s[:idx] + s[idx + k:]

    return s

s = "daabcbaabcbc"
part = 'abc'

print(removeOccurrences(s, part))



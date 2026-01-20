'''
A phrase is a palindrome if, after converting all uppercase letters 
into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters 
include letters and numbers.

Given a string s, return true if it is a palindrome, 
or false otherwise.
'''
def isalphaNum(ch):
    if (ch >= '0' and ch <= '9') or (ch.lower() >= 'a' and ch.lower() <= 'z'):
        return True
    return False


def validPalindrome(s):
    st , end = 0, len(s)-1

    while st < end:
        if isalphaNum(s[st]) is not True:
            st += 1
            continue
        if isalphaNum(s[end]) is not True:
            end -= 1
            continue
        if s[st].lower() != s[end].lower():
            return False
        st += 1
        end -= 1

    return True

s = "Ac3?e3c&a"
print(validPalindrome(s))


#Leet code solution subission
class Solution:
    def isalphaNum(self,ch):
        if (ch >= '0' and ch <= '9') or (ch.lower() >= 'a' and ch.lower() <= 'z'):
            return True
        return False


    def isPalindrome(self, s: str) -> bool:
        st , end = 0, len(s)-1

        while st < end:
            if self.isalphaNum(s[st]) is not True:
                st += 1
                continue
            if self.isalphaNum(s[end]) is not True:
                end -= 1
                continue
            if s[st].lower() != s[end].lower():
                return False
            st += 1
            end -= 1
        return True


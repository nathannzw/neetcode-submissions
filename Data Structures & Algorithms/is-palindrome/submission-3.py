# Two pointers O(n)/O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        
        return True 
        

'''
# Reverse string O(n)/O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = '' # to remove spaces and add only alphanumeric characters from original string

        # populate new_string
        for char in s:
            if char.isalnum():
                new_string += char.lower() # remember to handle casing
        
        return new_string == new_string[::-1]
'''
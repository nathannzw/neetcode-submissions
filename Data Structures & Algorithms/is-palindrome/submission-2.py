'''class Solution:
    def isPalindrome(self, s: str) -> bool:'''
        


# Reverse string O(n)/O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = '' # to remove spaces and add only alphanumeric characters from original string

        # populate new_string
        for char in s:
            if char.isalnum():
                new_string += char.lower() # remember to handle casing
        
        return new_string == new_string[::-1]
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''.join(e for e in s if e.isalnum())
        string = string.lower().strip()
        print(string)
        
        return string == string[::-1]
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Dictionary to count character frequencies
        freq_s = {}
        freq_t = {}
        
        # Count frequencies in s
        for char in s:
            if char in freq_s:
                freq_s[char] += 1
            else:
                freq_s[char] = 1
        
        # Count frequencies in t
        for char in t:
            if char in freq_t:
                freq_t[char] += 1
            else:
                freq_t[char] = 1
        
        # Compare frequency dictionaries
        return freq_s == freq_t

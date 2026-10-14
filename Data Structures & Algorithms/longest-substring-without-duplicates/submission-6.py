class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # basic sliding window approach
        char_set = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in char_set: # while right pointer element is a duplicate
                char_set.remove(s[l]) # remove left pointer element... 
                l += 1 # ...shrink window until no more duplicate
            char_set.add(s[r]) # add right pointer element to window set
            res = max(res, r - l + 1) # update longest valid substring length

        return res
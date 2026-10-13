class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {} # store character -> last seen index; window only goes from left to right
        l = 0 # start of window
        res = 0 # longest length result initialization

        for r in range(len(s)):
            if s[r] in mp:
              l = max(mp[s[r]] + 1, l) # move l pointer to one-right of seen index; max to enforce moving forwards
            mp[s[r]] = r # update last seen index of that element value
            res = max(res, r - l + 1)

        return res   

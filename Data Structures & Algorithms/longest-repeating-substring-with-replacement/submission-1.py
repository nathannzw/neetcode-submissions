class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window unoptimal approach
        char_set = set(s)
        res = 0

        for c in char_set: # check for each unique element
            l, count = 0, 0 # count of c inside window
            for r in range (l, len(s)):
                if s[r] == c:
                    count += 1
                while (r - l + 1) - count > k: # when replacment more than allowed, shrink window
                    if s[l] == c:
                        count -= 1 # decrement c frequency (replacements required)
                    l += 1 # shrink window

                res = max(res, (r - l + 1)) # update longest substring with length of valid window

        return res
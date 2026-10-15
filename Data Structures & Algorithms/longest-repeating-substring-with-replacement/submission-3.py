class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window optimal approach
        freq_dict, l, max_freq, res = defaultdict(int), 0, 0, 0
        for r in range(len(s)):
            freq_dict[s[r]] += 1 # accumulate frequency counts
            max_freq = max(max_freq, freq_dict[s[r]]) # update current max frequency
            while (r - l + 1) - max_freq > k: # if replacements needed more than constraint, shrink window
                freq_dict[s[l]] -= 1 # Decrement character leaving the window
                l += 1

            res = max(res, (r - l + 1)) # when reach this stage after while loop means the window is valid already

        return res
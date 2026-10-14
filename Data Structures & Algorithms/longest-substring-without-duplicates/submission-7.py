class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window using a dictionary to track character positions
        l = 0  # Left boundary of the current substring
        res = 0  # Longest valid substring length found so far
        last_index_dict = {}  # Stores each character's most recent index

        for r in range(len(s)):  # Move the right pointer through the string

            # If this character has appeared before
            if s[r] in last_index_dict:
                # Move left pointer past its previous occurrence,
                # but never move the left pointer backwards
                l = max(last_index_dict[s[r]] + 1, l)

            # Record the current character's index
            last_index_dict[s[r]] = r

            # Update the longest substring length (inclusive of both ends)
            res = max(res, r - l + 1)

        return res  # Return the longest length found
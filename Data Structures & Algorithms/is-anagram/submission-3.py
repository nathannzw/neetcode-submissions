class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # defaultdicts to store character counts
        s_count = defaultdict(int)
        t_count = defaultdict(int)

        # populate the count dictionaries
        for char in s:
            s_count[char] += 1
        for char in t:
            t_count[char] += 1

        # compare both dictionaries and return logic
        return s_count == t_count
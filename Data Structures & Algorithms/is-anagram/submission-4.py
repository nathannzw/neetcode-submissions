class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_dict = defaultdict(int)
        count_dict2 = defaultdict(int)

        for c in s:
            count_dict[c] += 1
        
        for c in t:
            count_dict2[c] += 1

        return count_dict == count_dict2
            
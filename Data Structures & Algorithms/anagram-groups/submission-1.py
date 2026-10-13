class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # count array -> strings
        for s in strs:
            count = [0] * 26 # create counter list for each string
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s) # need to convert to tuple because python cannot use list as key. also tuple is immutable
        return list(res.values())
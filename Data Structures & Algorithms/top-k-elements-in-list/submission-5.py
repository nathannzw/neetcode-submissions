class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int) # num -> frequency
        freq = [[] for i in range(len(nums) + 1)] # index is count of element and value is list of values that appear for that count because max length of freq is length of nums list

        # fill up the count hash map 
        for n in nums:
            count[n] += 1 

        # for each unique letter, append the specific number to the specific frequency list entry
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1): # traverse from highest frequency down, stop when required list length reached
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res



        
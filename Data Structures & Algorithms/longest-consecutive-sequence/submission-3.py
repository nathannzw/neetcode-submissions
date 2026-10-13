class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Hash Set Solution
        nums_set = set(nums) # unique elements only, lookup is O(n)
        longest = 0 # initialize longest sequence length counter

        for num in nums_set:
            if (num - 1) not in nums_set: # current num is the start of a sequence
                length = 1 # initialize current sequence length which is num 
                while (num + length) in nums_set: # while there are consecutive numbers
                    length += 1 # increment length by one and test above condition again
                longest = max(length, longest) # take max of current length and stored longest length so far

        return longest

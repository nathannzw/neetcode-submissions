class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {} # value->index pairs

        for i, val in enumerate(nums):
            diff = target - val
            # find diff in the dict
            # if inside, means came across before so return indices
            if diff in prev_map:
                return [prev_map[diff], i]
            # update the prev_map with current value if haven't returned
            prev_map[val] = i       

        return False



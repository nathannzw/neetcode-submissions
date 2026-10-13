class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # to store traversed values 
        # value -> index 
        prev_map = {}

        for i, val in enumerate(nums):
            # get other number that combines with current val to meet target
            diff = target - val

            # check if that other number has already been scanned/traversed
            if diff in prev_map:
                return [prev_map[diff], i] # return index of other number (from previous scan) and current

            # else, update the map based on current value and its index
            prev_map[val] = i

        return False # two sum failed, no valid solution



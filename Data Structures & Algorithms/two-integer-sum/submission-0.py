class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                twosum = nums[i] + nums[j]
                if twosum == target:
                    if i < j:
                        return [i, j]
                    else:
                        return [j, i]
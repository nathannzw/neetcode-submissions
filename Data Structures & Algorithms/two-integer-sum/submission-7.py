class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = defaultdict(int)
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diff_dict:
                return [i, diff_dict[diff]] if i < diff_dict[diff] else [diff_dict[diff], i]
            diff_dict[nums[i]] = i

        return 
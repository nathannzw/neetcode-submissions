class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            center_index = (l + r) // 2
            print(center_index)
            if nums[center_index] == target:
                return center_index
            elif nums[center_index] > target:
                r = center_index - 1
            else:
                l = center_index + 1

        return -1
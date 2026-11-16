class Solution:
    def findMin(self, nums: List[int]) -> int:
        # use binary search to find the cut
        l, r = 0, len(nums) - 1

        while l <= r:
            if l == r:
                return nums[l] # or nums[m]
            m = (l + r) // 2
            if nums[m] > nums[r]: # search at the top
                l = m + 1
            else:
                r = m
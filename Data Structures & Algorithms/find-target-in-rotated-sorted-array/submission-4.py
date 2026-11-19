class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            elif nums[l] <= nums[m]: # if left sub-array is clean (sorted), <= because l = m when one element left
                if target < nums[l] or target > nums[m]: # if target out of left clean sub-array
                    l = m + 1 # move search space to the right sub-array
                else: # if target within clean sorted left sub-array
                    r = m - 1 # close down search space to this left sub-array (normal binary search condition)
            else: # if right sub-array is clean (sorted)
                if target < nums[m] or target > nums[r]: # if target out of right clean sub-array
                    r = m - 1
                else: # if target within clean sorted right sub-array
                    l = m + 1

        return -1 

            
        
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # GOAL: smallest element of right sub-array
        l, r = 0, len(nums) - 1
        
        while l <= r:
            if l == r: # reached the single element which is min
                return nums[l] # or nums[r] same thing

            m = (l + r) // 2 # standard binary search find middle index
            
            if nums[m] > nums[r]: 
                # disjoint is located in current right sub-array
                l = m + 1 # move search space to the right
            else: # nums[m] <= nums[r]
                # disjoint is not here if reach this condition
                # just close search space until reach single element
                # which is the min
                r = m 

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
                l = m + 1 # reduce search space to the right
            else: # nums[m] <= nums[r]
                # disjoint located in current left sub-array
                r = m # reduce search space to the left

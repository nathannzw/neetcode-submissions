class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_dict = defaultdict(int)
        for num in nums:
            if duplicate_dict[num] >= 1:
                return True
            duplicate_dict[num] += 1
        return False
        
        
        #return len(set(nums)) < len(nums)
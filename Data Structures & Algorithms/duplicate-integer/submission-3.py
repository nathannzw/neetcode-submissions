class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
        
        
        '''count = defaultdict(int)
        for num in nums:
            print(count)
            if count[num] >= 1:
                return True
            count[num] += 1

        return False'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count_dict = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in count_dict:
                return [count_dict[diff], i]

            count_dict[num] = i

        return False
        
                

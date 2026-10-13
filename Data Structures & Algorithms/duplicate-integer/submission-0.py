class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_int = set()
        for num in nums:
            if num not in unique_int:
                unique_int.add(num)
            else:
                return True
        return False
         
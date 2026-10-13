class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique_integers = set(nums)

        count = {integer: 0 for integer in unique_integers}
        for num in nums:
            count[num] += 1
        sorted_items = sorted(count.items(), key=lambda x: x[1])  # Sort by values (x[1])
        sorted_keys = [item[0] for item in sorted_items]      # Extract keys
        return sorted_keys[:-k-1:-1]
        

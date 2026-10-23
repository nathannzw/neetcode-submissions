class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # maintain hash map of element value traversed before -> its index
        index_dict = defaultdict(int)

        for i in range(len(nums)):

            # get the other valid number paired with currently traversed element number
            diff = target - nums[i]
            
            # check if that valid number has been seen before
            if diff in index_dict:
                return [index_dict[diff], i]

            # add current number into index_dict
            index_dict[nums[i]] = i

        return 
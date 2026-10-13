class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0 # start pointer (to be incremented)
        j = len(numbers) - 1 # end pointer (to be decremented)

        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] > target:
                j -= 1
            if numbers[i] + numbers[j] < target:
                i += 1
            if i == j:
                return False

        return [i+1, j+1]
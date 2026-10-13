class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)

        while numbers[i] + numbers[j-1] != target:
            print(numbers[i], numbers[j-1])
            if numbers[i] + numbers[j-1] > target:
                j -= 1
            else:
                i += 1 

        return [i+1, j]
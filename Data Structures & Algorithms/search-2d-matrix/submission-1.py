class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # simple brute force
        for sublist in matrix:
            for element in sublist:
                if element == target:
                    return True

        return False
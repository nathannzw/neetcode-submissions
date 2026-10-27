class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Staircase search, start top right
        r, c = 0, len(matrix[0]) - 1
        while r < len(matrix) and r >= 0 and c < len(matrix[0]) and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                r += 1
            else:
                c -= 1

        return False
            
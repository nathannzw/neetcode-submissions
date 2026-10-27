class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 2-pass binary search: row-wise then column-wise
        top, bottom = 0, len(matrix) - 1 # initialize row pointers

        # perform binary search row-wise
        while top <= bottom:
            middle = (bottom + top) // 2
            if target < matrix[middle][0]:
                bottom = middle - 1
            elif target > matrix[middle][-1]:
                top = middle + 1
            elif matrix[middle][0] <= target and target <= matrix[middle][-1]:
                # perform binary search row-wise
                i, j = 0, len(matrix[0]) - 1
                while i <= j:
                    m = (j + i) // 2
                    if target == matrix[middle][m]:
                        return True
                    elif target < matrix[middle][m]:
                        j = m - 1
                    elif target > matrix[middle][m]:
                        i = m + 1
                return False
            else: 
                return False
                
        return False
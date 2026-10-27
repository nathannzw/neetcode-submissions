class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 1-pass binary search
        # REMEMBER THIS PATTERN FOR MATRIX:
        # row_index = m // number_cols
        # col_index = m % number_cols

        # treat matrix as single sorted area of size number_rows * number_cols
        # becomes simple binary search with extra conversion step to matrix coordinates
        
        l, r = 0, (len(matrix) * len(matrix[0])) - 1
        while l <= r:
            m = (l + r) // 2
            # convert to matrix coordinates
            row_index = m // len(matrix[0])
            col_index = m % len(matrix[0])
            if target == matrix[row_index][col_index]:
                return True
            elif target < matrix[row_index][col_index]:
                r = m - 1
            else:
                l = m + 1
        return False
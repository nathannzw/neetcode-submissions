class Solution:
    # hash set one pass solution
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        # for every particular entry'
        # traverse left->right->down->repeat
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                # check if specific entry in respective sets
                if (board[r][c] in rows[r] 
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]): # use tuple as key for squares
                    return False

                # update sets
                rows[r].add(board[r][c]) 
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        
        return True

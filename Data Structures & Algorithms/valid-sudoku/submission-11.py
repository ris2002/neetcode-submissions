class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Check each row
        for row in board:
            nums = [n for n in row if n != "."]
            if len(nums) != len(set(nums)):
                return False

        # Check each column
        for i in range(9):
            col = []
            for j in range(9):
                if board[j][i] != ".":
                    col.append(board[j][i])
            if len(col) != len(set(col)):
                return False

        # Check each 3x3 sub-box
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                square = []
                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):
                        if board[i][j] != ".":
                            square.append(board[i][j])
                if len(square) != len(set(square)):
                    return False

        # If all checks pass
        return True

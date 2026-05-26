class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            row_count={}
            for num in row:
                if num not in row_count:
                    row_count[num]=0
                row_count[num]+=1
                if row_count[num]>1 and num!=".":
                    return False
                else:
                    continue
        
        n=len(board)
        for i in range(n):
            col_count={}
            for col in board:
                if col[i] not in col_count:
                    col_count[col[i]]=0
                col_count[col[i]]+=1
                if col_count[col[i]]>1 and col[i]!=".":
                    return False
                else:
                    continue
        
        for row_start in range(0,n,3):
            for col_start in range(0,n,3):
                sq_count={}
                for i in range(row_start,row_start+3):
                    for j in range(col_start,col_start+3):
                        a=board[i][j]
                        if a not in sq_count:
                            sq_count[a]=0
                        sq_count[a]+=1
                        if a!=".":
                            if sq_count[a]>1:
                                return False
        return True




            

                

        
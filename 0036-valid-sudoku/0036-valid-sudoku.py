class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[ set() for _ in range (9)]
        cols=[set()for _ in range(9)]
        boxes=[set()for _ in range(9)]

        for i in range (9):
            for j in range(9):
                val=board[i][j]
                if val==".":
                    continue
                if val in rows[i]:
                    return False
                rows[i].add(val)
                if val in cols[j]:
                    return False
                cols[j].add(val) 
                box_index=(i//3)*3+(j//3)
                if val in boxes[box_index]:
                    return False
                boxes[box_index].add(val)
        return True
                
    # def checkrow(self, board: List[List[str]])  -> bool:
    #     for i in range (0,9):
    #         arr=[]
    #         for j in range (0,9):
    #             if board[i][j] == ".":
    #                 continue
    #             else:
    #                 if board[i][j] in arr:
    #                     return False
    #                     # return arr
    #                 else:
    #                     arr.append(board[i][j])
    #     return True
    
    # def checkcol(self,board: List[List[str]])  -> bool:
    #     for i in range (0,9):
    #         arr=[]
    #         for j in range (0,9):
    #             if board[j][i] == ".":
    #                 continue
    #             else:
    #                 if board[j][i] in arr:
    #                     return False
    #                     # return arr
    #                 else:
    #                     arr.append(board[j][i])
    #     return True
    
    # def checkbox(self,board: List[List[str]])  -> bool:
    #     for box_row in range (0,9,3):
    #         for box_col in range (0,9,3):
    #             arr=[]
    #             for i in range (3):
    #                 for j in range (3):
    #                     val=board[box_row+i][box_row+j]
    #                     if val==".":
    #                         continue
    #                     if val in arr:
    #                         return False
    #                     arr.append(val)
    #     return True

    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     return self.checkrow(board) and self.checkcol(board) and self.checkbox(board)

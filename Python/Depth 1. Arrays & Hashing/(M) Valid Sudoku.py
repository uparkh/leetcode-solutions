class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rowSets = [set() for i in range(9)]
        colSets = [set() for i in range(9)]
        subset3x3 = [set() for i in range(9)]

        for i, row in enumerate(board):
            for j in range(len(row)):
                elem = board[i][j]
                subset3x3Index = 3*(i//3) + j//3
                if elem == ".": continue

                if elem in rowSets[i]: return False
                if elem in colSets[j]: return False
                if elem in subset3x3[subset3x3Index]: return False

                rowSets[i].add(elem)
                colSets[j].add(elem)
                subset3x3[subset3x3Index].add(elem)

        return True


board = [["5","3",".",".","7",".",".",".","."]
        ,["6","8",".","1","9","5",".",".","."]
        ,[".","9","4",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board))

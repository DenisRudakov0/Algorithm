def done_or_not(board):
    lis = []
    if len(board) == 0:
        return 'Try again!'
    if [9 for i in range(len(board))].count(9) != 9:
        return 'Try again!'
    for i in range(0, 9):
        for j in range(0, 9):
            lis = [board[i][j] for i in range(0, 9)]
            if lis.count(board[i][j]) > 1:
                return 'Try again!'
            elif board[i].count(board[i][j]) > 1:
                return 'Try again!'

            
            lis1 = []
            if i in [0, 3, 6] and j in [0, 3, 6]:
                for k in range(3):
                    lis1.extend([board[k][i] for i in range(j, j + 3)])
                if lis1.count(board[i][j]) > 1:
                    return 'Try again!'
            elif i in [1, 4, 7] and j in [1, 4, 7]:
                for k in range(3):
                    lis1.extend([board[k][i] for i in range(j - 1, j + 2)])
                if lis1.count(board[i][j]) > 1:
                    return 'Try again!'
            elif i in [2, 5, 8] and j in [2, 5, 8]:
                for k in range(3):
                    lis1.extend([board[k][i] for i in range(j - 2, j + 1)])
                if lis1.count(board[i][j]) > 1:
                    return 'Try again!'           
            
    return 'Finished!'

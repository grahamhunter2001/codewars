ef validSolution(board):
    for row in board:
        avail_nums = set([1,2,3,4,5,6,7,8,9])
        try:
            for val in row:
                avail_nums.remove(val)
        except: return False

    for col in range(len(board[0])):
        avail_nums = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
        for row in range(len(board)):
            try:
                avail_nums.remove(board[row][col])
            except: return False

    start_pos = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
    for item in start_pos:
        avail_nums = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
        try:
            for i in range(3):
                row = item[0] + i
                for j in range(3):
                    col = item[1] + j
                    avail_nums.remove(board[row][col])
        except: return False
    return True

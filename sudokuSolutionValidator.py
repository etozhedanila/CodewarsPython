def validSolution(board):
	result = True

	for i in range(len(board)):
		rowSet = set()
		colSet = set()
		boxSet = set()
		for j in range(len(board[i])):
			if board[i][j] == 0:
				return False
			rowSet.add(board[i][j])
			colSet.add(board[j][i])

			if i % 3 == 0 and j % 3 == 0:
				boxSet.add(board[i][j])
				boxSet.add(board[i + 1][j])
				boxSet.add(board[i + 2][j])
				boxSet.add(board[i][j + 1])
				boxSet.add(board[i][j + 2])
				boxSet.add(board[i + 1][j + 1])
				boxSet.add(board[i + 1][j + 2])
				boxSet.add(board[i + 2][j + 1])
				boxSet.add(board[i + 2][j + 2])
				if len(boxSet) != 9:
					return False
				
		if len(rowSet) != 9 or len(colSet) != 9:
			return False


	return result


a = validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                   [6, 7, 2, 1, 9, 5, 3, 4, 8],
                   [1, 9, 8, 3, 4, 2, 5, 6, 7],
                   [8, 5, 9, 7, 6, 1, 4, 2, 3],       
                   [4, 2, 6, 8, 5, 3, 7, 9, 1],
                   [7, 1, 3, 9, 2, 4, 8, 5, 6],
                   [9, 6, 1, 5, 3, 7, 2, 8, 4],
                   [2, 8, 7, 4, 1, 9, 6, 3, 5],
                   [3, 4, 5, 2, 8, 6, 1, 7, 9]])

print(a)
# # Recursive solution for N-Queens problem in Python

# from math import *
# import sys


# def printSolution(board, n):
#     for i in range(n):
#         for j in range(n):
#             print(board[i][j], end=' ')
#         print()


# def isSafe(board, row, col, n):
#     for i in range(col):
#         if board[row][i] == 1:
#             return False

#     for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
#         if board[i][j] == 1:
#             return False

#     # Check lower diagonal on left side
#     for i, j in zip(range(row, n, 1), range(col, -1, -1)):
#         if board[i][j] == 1:
#             return False

#     return True


# def solve_nqueens(board, col, n):
#     if col >= n:
#         return True

#     for i in range(n):

#         if isSafe(board, i, col, n):
#             # Place this queen in board[i][col]
#             board[i][col] = 1

#             # recur to place rest of the queens
#             if solve_nqueens(board, col + 1, n):
#                 return True

#             board[i][col] = 0

#     return False


# def main():
#     n = int(input())
#     # n = 3
#     board = [[0] * n for i in range(n)]
#     if not solve_nqueens(board, 0, n):
#         print("Solution does not exist")
#         return False
#     print()
#     printSolution(board, n)
#     return True


# if __name__ == "__main__":
#     main()

col = []
dig1 = []
dig2 = []
arr = []
n = (int)(input())
for i in range(0, n):
	col.append(0)
	arr.append(-1)
for i in range(0, 2 * n):
	dig1.append(0)
	dig2.append(0)

def feasible(r, c):
	if(col[c] == 1):
		return False
	if(dig1[r + c] == 1):
		return False
	if(dig2[r - c + n] == 1):
		return False
	return True
def nqueen(r):
	if r == n:
		return True

	for i in range(0, n):
		if(feasible(r, i)):
			arr[r] = i
			col[i] = 1
			dig1[r + i] = 1
			dig2[r - i + n] = 1
			if(nqueen(r + 1)):
				return True
			arr[r] = -1
			col[i] = 0
			dig1[r + i] = 0
			dig2[r - i + n] = 0
	return False

if(nqueen(0)):
	for i in range(0, n):
		for j in range(0, n):
			if arr[i] == j:
				print("Q ", end = "")
			else :
				print("0 ", end = "")
		print()
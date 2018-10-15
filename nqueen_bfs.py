from queue import Queue
from copy import deepcopy

def isSafe(board, row, col, n):

    # check left row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def n_queens_bfs(q, board, n):
    while not q.empty():
        cur_state = q.get()
        # print(cur_state)
        # cur_state = list(cur_state)
        cur_board = cur_state[0]
        col = cur_state[1]
        print(cur_board)
        print(col)
        for i in range(n):

            # print(cur_board)
            if isSafe(cur_board, i, col, n):
                cur_board[i][col] = 1
                # print("haa")
                # print(cur_board, col+1)
                q.put((deepcopy(cur_board), col+1))
                if col == n - 1:
                    # print("Yes")
                    return cur_board
                cur_board[i][col] = 0
    # print("yes")
    return False

def main():
    n = int(input())
    board = [[0] * n for i in range(n)]
    q = Queue()
    q.put((board, 0))
    sol = n_queens_bfs(q, board, n)
    if not sol:
        print("No Solution")
    else:
        for x in sol:
            for y in x:
                print(y, end = '   ')
            print('\n')

if __name__== "__main__":
    main()
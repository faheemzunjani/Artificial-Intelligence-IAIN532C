import heapq
import numpy as np
import argparse
from itertools import count

tiebreaker = count()

parser = argparse.ArgumentParser()
parser.add_argument('--n', nargs='?', const=4, default = 4, type=int)
args = parser.parse_args()
N = args.n

board = np.zeros((N, N),dtype = int)

def Astar():
    q=[]
    heapq.heapify(q)
    heapq.heappush(q,(g(board),0,0,board))
    while len(q):
        f , c ,n , b = heapq.heappop(q)#pops the one with least priprity value
        if(n == N):
            printSolution(b)
            return
        children = generate_children(b , n)
        if len(children) == 0:
            continue
        for i in range(len(children)):
            heapq.heappush(q,(N-children[i][0]+g(children[i][1]),next(tiebreaker),children[i][0],children[i][1]))
    
def isSafe(b,m,n):
    for i,j in zip(range(m,-1,-1) , range(n,-1,-1)):
        if(b[i][j] == 1):
            return False
    for i,j in zip(range(m , -1, -1) , range(n , N)):
        if(b[i][j] == 1):
            return False
    for i,j in zip(range(m,N) , range(n,-1,-1)):
        if(b[i][j] == 1):
            return False
    for i in range(0 , N):
        if(b[i][n] == 1 or b[m][i] ==1):
            return False
    return True

def generate_children(b , n):
    children = []
    for i in range(N):
        child = np.copy(b)
        child[n][i] = 1
        if isSafe(b,n,i):
            children.append([n+1,child])

    return children


def g(b):
    count = 0
    for i in range(N):
        for j in range(N):
            if not b[i][j]==1 and isSafe(b,i,j):
                count = count + 1

    return count
def printSolution(b):
    for i in range(N):
        for j in range(N):
            print(str(b[i][j]) + "|", end = ' ')
        print()
        print("---"*N)

def nth_largest(n, iter_list):
    length = len(iter_list)
    if n >= length:
        return heapq.nlargest(length, iter_list)[-1]
    return heapq.nlargest(n, iter_list)[-1]



Astar()
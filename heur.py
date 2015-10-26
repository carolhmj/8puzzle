from State import State
from collections import deque
import math

def find_piece (piece, puzzle):
	for i,pi in enumerate(puzzle):
		for j,pj in enumerate(pi):
			if piece == puzzle[i][j]: 
				return (i,j)

def heur_man (pz1, pz2):
	sum = 0
	for i,pi in enumerate (pz1):
		for j,pj in enumerate (pi):
			if pj != 0:
				(a,b) = find_piece(pj, pz2)
				sum = sum + (abs(i-a) + abs(j-b))
	return sum

def heur_min (pz1, pz2):
	sum = 0
	for i,pi in enumerate (pz1):
		for j,pj in enumerate (pi):
			if pj != 0:
				(a,b) = find_piece(pj, pz2)
				if (i!=a or j!=b):
					sum = sum+1
	return sum

def heur_sane (pz1,pz2):
	return 0

# def main():
# 	i = [[0, 6, 8], [1, 7, 2], [4, 5, 3]]
# 	j = [[0, 6, 8], [1, 7, 2], [4, 5, 3]]
# 	print heur_min (i,j)


# if __name__ == "__main__":
#     main()
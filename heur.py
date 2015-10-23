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

def main():
	i = [[0, 6, 8], [2, 7, 1], [4, 5, 3]]
	j = [[3, 8, 6], [2, 7, 1], [4, 5, 0]]
	print heur_man (i,j)


if __name__ == "__main__":
    main()
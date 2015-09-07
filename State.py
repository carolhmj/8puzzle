#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy

class State:
	""""State é uma classe que representa um estado do 8-puzzle. Ela possui uma variável de classe que indica o valor do espaço vazio
	no puzzle, uma que indica a dimensão (no caso, 3), e também possui uma variável que guarda o estado do puzzle em uma matriz
	quadrada de dimensão dimension, e uma variável que guarda a posição do espaço vazio em uma tupla"""
	emptyValue = -1
	dimension = 3
	def __init__(self, puzzle, emptyPos):
		if len(puzzle) == self.dimension and len(puzzle[0]) == self.dimension:
			self.puzzle = puzzle
		if emptyPos[0] >= 0 and emptyPos[0] < self.dimension and emptyPos[1] >= 0 and emptyPos[1] < self.dimension:
			self.emptyPos = emptyPos
	def printState(self):
		"""Imprime o estado no terminal, para visualização"""
		print("========================")
		for i in self.puzzle:
			print("| "),
			for j in i:
				print(j),
				print(" |"),
			print("")
		print("========================")
	def insertPosT(self, elem, intuple):
		"""Retorna uma posição a partir de uma tupla"""
		self.puzzle[intuple[0]][intuple[1]] = elem		
	def nextStates(self):
		"""Baseada no seu estado atual, essa função retorna uma lista de States que representam os movimentos possíveis"""
		returnedStates = []

		upNeighbor = (self.emptyPos[0]-1, self.emptyPos[1])
		if upNeighbor[0] >= 0:
			"""Se o vizinho de cima da posição do vazio existe, existe um estado obtido trocando a posição do vazio pelo objeto
			no vizinho de cima. Usando deepcopy porque a operação de assigment em Python só faz um objeto referenciar outro,
			e não queremos que o puzzle original mude"""		
			stateUpPuzzle = deepcopy(self.puzzle)
			stateUpPuzzle[self.emptyPos[0]][self.emptyPos[1]] = deepcopy(self.puzzle[upNeighbor[0]][upNeighbor[1]])
			stateUpPuzzle[upNeighbor[0]][upNeighbor[1]] = self.emptyValue

			stateUp = State(stateUpPuzzle, upNeighbor)
			returnedStates.append(stateUp)


		downNeighbor = (self.emptyPos[0]+1, self.emptyPos[1])
		if downNeighbor[0] < self.dimension:
			"""Se o vizinho de cima da posição do vazio existe, existe um estado obtido trocando a posição do vazio pelo objeto
			no vizinho de cima. Usando deepcopy porque a operação de assigment em Python só faz um objeto referenciar outro,
			e não queremos que o puzzle original mude"""		
			stateDownPuzzle = deepcopy(self.puzzle)
			stateDownPuzzle[self.emptyPos[0]][self.emptyPos[1]] = deepcopy(self.puzzle[downNeighbor[0]][downNeighbor[1]])
			stateDownPuzzle[downNeighbor[0]][downNeighbor[1]] = self.emptyValue

			stateDown = State(stateDownPuzzle, downNeighbor)
			returnedStates.append(stateDown)
			
		leftNeighbor = (self.emptyPos[0], self.emptyPos[1]-1)
		if leftNeighbor[1] >= 0:
			"""Se o vizinho de cima da posição do vazio existe, existe um estado obtido trocando a posição do vazio pelo objeto
			no vizinho de cima. Usando deepcopy porque a operação de assigment em Python só faz um objeto referenciar outro,
			e não queremos que o puzzle original mude"""		
			stateLeftPuzzle = deepcopy(self.puzzle)
			stateLeftPuzzle[self.emptyPos[0]][self.emptyPos[1]] = deepcopy(self.puzzle[leftNeighbor[0]][leftNeighbor[1]])
			stateLeftPuzzle[leftNeighbor[0]][leftNeighbor[1]] = self.emptyValue

			stateLeft = State(stateLeftPuzzle, leftNeighbor)
			returnedStates.append(stateLeft)
			
		rightNeighbor = (self.emptyPos[0], self.emptyPos[1]+1)
		if rightNeighbor[1] < self.dimension:
			"""Se o vizinho de cima da posição do vazio existe, existe um estado obtido trocando a posição do vazio pelo objeto
			no vizinho de cima. Usando deepcopy porque a operação de assigment em Python só faz um objeto referenciar outro,
			e não queremos que o puzzle original mude"""		
			stateRightPuzzle = deepcopy(self.puzzle)
			stateRightPuzzle[self.emptyPos[0]][self.emptyPos[1]] = deepcopy(self.puzzle[rightNeighbor[0]][rightNeighbor[1]])
			stateRightPuzzle[rightNeighbor[0]][rightNeighbor[1]] = self.emptyValue

			stateRight = State(stateRightPuzzle, rightNeighbor)
			returnedStates.append(stateRight)		

		return returnedStates

	def __eq__(self, secondState):
		"""Compara dois estados, retorna verdadeiro se eles são iguais"""
		if isinstance(secondState, self.__class__):
			joinedStates = zip(self.puzzle, secondState.puzzle)
			for j in joinedStates:
				joinedElem = zip(j[0],j[1])
				for l in joinedElem:
					if l[0] != l[1]:
						return False
			return True
		else:
			return False
			
	def __neq__(self, secondState):
		return not self.__eq__(secondState)			

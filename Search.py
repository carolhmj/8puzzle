#!/usr/bin/env python
# -*- coding: utf-8 -*-

from State import State
from collections import deque
from heur import heur_man
from heapq import *
import math


class BFSearch(object):
	"""Classe responsável por realizar a busca de um estado inicial para um estado final"""
	def __init__(self, initialState, finalState):
		"""Possui um estado inicial, de onde começa a busca, e um estado final, onde ela termina a busca"""
		self.initialState = initialState
		self.finalState = finalState
	def changeInitial(self, newInitial):
		self.initialState = newInitial
	def changeFinal(self, newFinal):
		self.finalState = newFinal
	def runSearch(self):
		"""Por enquanto, uma busca em largura simples. Eventualmente pode mudar pra uma busca A*?"""
		#print("EHN2")
		searchStates = deque()
		searchStatesSet = set()
		searchStates.append(self.initialState)
		searchStatesSet.add(self.initialState)
		#visitedStates = []
		visitedStatesSet = set()

		count = 0
		while len(searchStates) > 0:
			currentState = searchStates.popleft()
			#currentState.printState()
			count = count + 1
			#if (count == math.factorial(9)/2):
			#	print(":(")
			#	return None
			print(count)
			#visitedStates.append(currentState)
			visitedStatesSet.add(currentState)
			for nextState in currentState.nextStates():
				#nextState.printState()
				if nextState == self.finalState:
					return nextState.constructPath()
				elif (nextState not in visitedStatesSet) and (nextState not in searchStatesSet):
					searchStates.append(nextState)
					searchStatesSet.add(nextState)
			

		print("Busca falhou")
		return None

class AStarSearch(object):
	"""Classe responsável por realizar a busca de um estado inicial para um estado final"""
	def __init__(self, initialState, finalState, heuristic):
		"""Possui um estado inicial, de onde começa a busca, e um estado final, onde ela termina a busca"""
		self.initialState = initialState
		self.finalState = finalState
		self.heuristic = heuristic
	def changeInitial(self, newInitial):
		self.initialState = newInitial
	def changeFinal(self, newFinal):
		self.finalState = newFinal

		
	def runSearch(self):
		"""Por enquanto, uma busca em largura simples. Eventualmente pode mudar pra uma busca A*?"""
		searchStates = []
		searchStatesSet = set()
		heappush(searchStates,((self.initialState.height + self.heuristic(self.initialState.puzzle, self.finalState.puzzle)), self.initialState))
		searchStatesSet.add(self.initialState)
		visitedStatesSet = set()

		count = 0
		while len(searchStates) > 0:
			(_,currentState) = heappop(searchStates)
			count = count + 1
			print(count)
			visitedStatesSet.add(currentState)
			for nextState in currentState.nextStates():
				#nextState.printState()
				if nextState == self.finalState:
					return nextState.constructPath()
				elif (nextState not in visitedStatesSet) and (nextState not in searchStatesSet):
					heappush(searchStates,((nextState.height + self.heuristic(nextState.puzzle, self.finalState.puzzle)), nextState))
					searchStatesSet.add(nextState)
			

		print("Busca falhou")
		return None		
__author__ = "Siddharth Vasudevan"

import sys
import heapq

class Edge(object):

	def __init__(self, weight, startVertex, targetVertex):
		self.weight = weight
		self.startVertex = startVertex
		self.targetVertex = targetVertex
		
class Node(object):

	def __init__(self, name):
		self.name = name
		self.visited = False
		self.predecessor = None
		self.adjacenciesList = []
		self.minDistance = sys.maxsize
		
	def __cmp__(self, otherVertex):
		return self.cmp(self.minDistance, otherVertex.minDistance)
		
	def __lt__(self, other):
		selfPriority = self.minDistance
		otherPriority = other.minDistance
		return selfPriority < otherPriority

class Algorithm(object):

	def calculateShortestPath(self, vertexList, startVertex):
	
		q = []
		startVertex.minDistance = 0
		heapq.heappush(q, startVertex)
		
		while q:
		
			actualVertex = heapq.heappop(q)
			
			for edge in actualVertex.adjacenciesList:
				u = edge.startVertex
				v = edge.targetVertex
				newDistance = u.minDistance + edge.weight
				
				if newDistance < v.minDistance:
					v.predecessor = u
					v.minDistance = newDistance
					heapq.heappush(q, v)
					
	def getShortestPathTo(self, targetVertex):
		# print("Shortest path to vertex is: ", targetVertex.minDistance)
		
		node = targetVertex
		
		while node is not None:
			print("%s " % node.name)
			node = node.predecessor
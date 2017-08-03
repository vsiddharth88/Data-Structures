__author__ = "Siddharth Vasudevan"

import heapq;

class Graph(object):
	def __init__(self,verts)
		self.verts = verts

class Vertex(object):

	def __init__(self, name):
		self.name = name;
		self.visited = False;
		self.predecessor = None;
		self.adjList = [];
		
	def __str__(self):
		return self.name;
		
class Edge(object):

	def __init__(self, weight, sV, tV):
		self.weight = weight;
		self.sV = sV;
		self.tV = tV;
		
	def __cmp__(self, other):
		return self.cmp(self.weight, other.weight);
		
	def __lt__(self, other):
		selfPriority = self.weight;
		otherPriority = other.weight;
		return selfPriority < otherPriority;

	def otherEnd(u):
		if self.sV == u:
			return sV
		else
			return tV
	
	
class PrimsJarnik(object):

	def __init__(self, unVistList):
		self.unVistList = unVistList;
		self.spanningTree = [];
		self.edgeHeap = [];
		self.fullCost = 0;
		
	def SpanningTree(self, vertex):
	
		self.unVistList.remove(vertex);
		
		while self.unVistList:
		
			for edge in vertex.adjList:
				if edge.tV in self.unVistList:
					heapq.heappush(self.edgeHeap, edge);
					
			minEdge = heapq.heappop(self.edgeHeap);
			
			self.spanningTree.append(minEdge);
			print("Edge added to spanning tree: %s - %s" % (minEdge.sV.name, minEdge.tV.name));
			self.fullCost = self.fullCost + minEdge.weight;
			
			vertex = minEdge.tV;
			self.unVistList.remove(vertex);

	def getSpanningTree(self):
		return self.spanningTree;
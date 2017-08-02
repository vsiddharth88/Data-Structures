__author__ = "Siddharth Vasudevan"

class Vertex(object):

	def __init__(self, name):
		self.name = name
		self.node = None
		
class Node(object):

	def __init__(self, height, nodeId, parentNode):
		self.height = height
		self.nodeId = nodeId
		self.parentNode = parentNode
		
class Edge(object):
	
	def __init__(self, weight, startVertex, targetVertex):
		self.weight = weight
		self.startVertex = startVertex
		self.targetVertex = targetVertex
		
	def __cmp__(self, otherEdge):
		return self.cmp(self.weight, otherEdge.weight)
		
	def __lt__(self, other):
		selfPriority = self.weight
		otherPriority = other.weight
		return selfPriority < otherPriority
		
class DisjointSet(object):

	def __init__(self, vertexList):
		self.vertexList = vertexList
		self.rootNodes = []
		self.nodeCount = 0
		self.setCount = 0
		self.makeSets(vertexList)
		
	def find(self, node):
	
		currentNode = node
		
		while currentNode.parentNode is not None:
			currentNode = currentNode.parentNode
			
		root = currentNode
		currentNode = node
		
		while currentNode is not root:
			temp = currentNode.parentNode
			currentNode.parentNode = root
			currentNode = temp
			
		return root.nodeId
	
	def merge(self, node1, node2):
	
		index1 = self.find(node1)
		index2 = self.find(node2)
		
		if index1 == index2:
			return
			
		root1 = self.rootNodes[index1]
		root2 = self.rootNodes[index2]
		
		if root1.height < root2.height:
			root1.parentNode = root2
		elif root1.height > root2.height:
			root2.parentNode = root1
		else:
			root2.parentNode = root1
			root1.height = root1.height + 1
		
	def makeSets(self, vertexList):
		for v in vertexList:
			self.makeSet(v)
			
	def makeSet(self, vertex):
		node = Node(0, len(self.rootNodes),None)
		vertex.node = node
		self.rootNodes.append(node)
		self.setCount = self.setCount + 1
		self.nodeCount = self.nodeCount + 1
		
class KruskalAlgorithm(object):

	def spanningTree(self, vertexList, edgeList):
	
		disjointSet = DisjointSet(vertexList)
		spanningTree = []
		
		edgeList.sort()
		
		for edge in edgeList:
		
			u = edge.startVertex
			v = edge.targetVertex
			
			if disjointSet.find(u.node) is not disjointSet.find(v.node):
				spanningTree.append(edge)
				disjointSet.merge(u.node, v.node)
				
		for edge in spanningTree:
			print(edge.startVertex.name," - ", edge.targetVertex.name)

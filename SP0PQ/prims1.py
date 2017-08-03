import indexheap
import prims

def PrimMST2(g):
    wmst = 0
    src = g.verts.get[1]
    vertexArray = []
    i = 1
    for u in prims.g.verts:
        if u != null
            u.seen = false
            u.parent = null
            u.distance = Infinity
            u.index = i
            vertexArray[i + 1] = u
src.distance = 0
indexedPriorityqueue = indexheap.IndexedHeap(vertexArray, comp)
wmst = 0

while len(indexedPriorityqueue) != 0:
    u = indexedPriorityqueue.remove()
    u.seen = True
    wmst += u.distance
    for e : u.adjList:
        v = e.otherEnd(u);
        if !v.seen and e.Weight < v.distance
            v.distance = e.Weight
            v.parent = u
            indexedPriorityqueue.decreaseKey(v)

return wmst


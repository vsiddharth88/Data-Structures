__author__ = 'Siddharth Vasudevan'

import binheap

class IndexedHeap(binheap.Heap):
    def percolateDown(self,i):
    	x = self.data[i]
    	while 2*i <= self.size:
    		if 2*i ==self.size:
    			if x > self.data[self.size]:
    				self.data[i] = self.data[self.size]
    				self.data[i].putIndex(i)
    				i = self.size
                else:
    				break
           else:
    			smallChild = 0
    			if self.data[2*i] <= self.data[2*i+1]:
    				smallChild = 2*i
                else:
    				smallChild = 2*i+1
    			if x > self.data[smallChild]:
    				self.data[i] = self.data[smallChild]
    				self.data[i].putIndex(i)
    				i = smallChild
    			else
    				break
    	self.data[i] = x
    	self.data[i].putIndex(i)
    
    def percolateUp(i): 
    	self.data[0] = self.data[i]
    	while self.data[i/2] > self.data[0]:
    		self.data[i] = self.data[i/2]
    		self.data[i].putIndex(i)
    		i = i/2
    	self.data[i] = self.data[0];
    	self.data[i].putIndex(i);




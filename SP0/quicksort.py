__author__ = 'Siddharth Vasudevan'

import random

def swap(x,y,inputElements):
	temp = inputElements[x]
	inputElements[x] = inputElements[y]
	inputElements[y] = temp

def circularSwap(i,j,l,inputElements):
	if i == l:
		swap(i, j, inputElements)
		return
	temp1 = inputElements[j]
	inputElements[j] = inputElements[i]
	temp2 = inputElements[l]
	inputElements[l] = temp1
	inputElements[i] = temp2

def multiPivotPartitionByRandomPivot(inputElements,p,r):
	index1 = random.randint(p,r-p+1)
	index2 = random.randint(p,r-p+1)
	if inputElements[index1] <= inputElements[index2]:
		swap(p, index1, inputElements)
		swap(r, index2, inputElements)
		if inputElements[p] > inputElements[r]:
			swap(p, r, inputElements)
	else:
		swap(r, index1, inputElements)
		swap(p, index2, inputElements)
		if inputElements[p] > inputElements[r]:
			swap(p, r, inputElements)
	x1 = inputElements[p]
	x2 = inputElements[r]
	l = p+1
	i = l
	j = r-1
	while i <=j and l<r:
		if x1 < inputElements[i] and x2 >= inputElements[i]:
			i += 1
		elif inputElements[i] < x1:
			swap(i, l, inputElements)
			l += 1
			i += 1
		elif inputElements[j] > x2:
				j -=1
		elif inputElements[i] > x2 and inputElements[j] < x2:
			circularSwap(i, j, l, inputElements)
			l += 1
			i += 1
			j -= 1
		elif inputElements[i] > x2 and x1 <= inputElements[j] <= 0 and x2 >= inputElements[j]:
			swap(i, j, inputElements)
			i += 1
			j -= 1
	swap(p, l - 1, inputElements)
	swap(j + 1, r, inputElements)
	return  (l-1,x1,x2,j+1)


def quickSortRandom(inputElements, p, r):
	if p < r:
		pr = multiPivotPartitionByRandomPivot(inputElements, p, r)
		quickSortRandom(inputElements, p, pr[0]- 1)
		if pr[1] == pr[2]:
			quickSortRandom(inputElements, pr[0]+ 1, pr[3] - 1)
		quickSortRandom(inputElements, pr[3] + 1, r)


input1 = [100,33,1,98,24,56,39,41,23]
quickSortRandom(input1,0,len(input1)-1)
print(input1)

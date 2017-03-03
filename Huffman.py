class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

def delMin(H):
	global currentSize
	
	retval = H[1]
	
	H[1] = H[currentSize]
	# print 'this is H1',H
	# print
	# print 'currentSize in delMin1', currentSize
	# print
	currentSize = currentSize - 1
	# print 'currentSize in delMin2', currentSize
	# print
	H.pop()
	# print 'this is H2 after pop',H
	# print
	percDown(1)

	return retval

def percDown(i):
	    while (i * 2) <= currentSize:
	    	# print 'this is currentSize',currentSize
	    	# print
	        mc = minChild(i)
	        # print 'this is mc',mc
	        # print
	        if H[i][1] > H[mc][1]:
	            tmp = H[i]
	            H[i] = H[mc]
	            H[mc] = tmp
	        i = mc

def minChild(i):
	    if i * 2 + 1 > currentSize:
	        return i * 2
	    else:
	    	# print 'this is i in minChild', i
	    	# print
	        if H[i*2][1] < H[i*2+1][1]:
	            return i * 2
	        else:
	            return i * 2 + 1

def percUp(i):
	while i // 2 > 0:
		if H[i][1] < H[i // 2][1]:
			tmp = H[i // 2]
			H[i // 2] = H[i]
			H[i] = tmp
		i = i // 2

def insert(k):
	global currentSize
	H.append(k)
	# print 'this is H in insert',H
	# print
	currentSize = currentSize + 1
	percUp(currentSize)

def stringToFreq(stringInput):
	global S, f, n

	S = list(stringInput)
	S = dict.fromkeys(stringInput).keys()
	S.sort()
	n = len(S)

	f = []
	for w in S:
		f.append(stringInput.count(w))

	a = 0
	f = [a] + f
	S = [a] + S
	
	return S, f

inputString="AAABBBBCCDEIIz"
print 'these are my S and f arrays',stringToFreq(inputString)
print

################################
## begin the Huffman tree here##
################################


def huffmanEncode(S,f):
	global H

	H = []
	n = len(f)

	# this for loop makes the min heap
	for i in range(0,n):

		H.append([S[i],f[i]])
		H = sorted(H, key=lambda H: H[1])

	return H




H =  huffmanEncode(S,f)
currentSize = len(H) - 1

# print 'this is my H after huffmanEncode',H
# print

# i = delMin(H)
# print 'this is i', i
# print

# print 'H after delMin called for i',H
# print

# j = delMin(H)
# print 'this is j',j
# print

# print 'H after delMin called for j',H
# print

# k = [i[0]+j[0],i[1]+j[1]]
# print 'this is k',k

# insert(k)

# print 'this is H after K insert',H
# print

while currentSize != 1:
	print 'this is H:',H
	print
	i = delMin(H)
	j = delMin(H)
	k = [i[0]+j[0],i[1]+j[1]]
	# insert(k)

	left = i
	right = j
	tree = Tree(k,left,right)
	insert(tree)
	

print 'this is final H:',H
print

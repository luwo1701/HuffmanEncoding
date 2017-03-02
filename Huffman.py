inputString="AAABBBBBBBBCCDEFFFFFFGIIIIJJz"

class Tree:
	def __init__(self, cargo, left=None, right=None):
		self.cargo = cargo
		self.left  = left
		self.right = right

		def __str__(self):
			return str(self.cargo)

# must be able to look through alphabet and other unique characters
# is also case sensitive

# print the histogram and then number of unique characters in the string



def stringToFreq(stringInput):
	global S, f, n

	S = list(stringInput)
	S=dict.fromkeys(stringInput).keys()
	S.sort()
	n = len(S)

	f = []
	for w in S:
		f.append(stringInput.count(w))

	# adding a zero to the each array to make
	# indexing easy
	a = 0
	f = [a] + f
	S = [a] + S

	return S, f



print stringToFreq(inputString)

	

def huffmanEncode(S,f):

	H = []
	n = len(f)

	for i in range(0,n):

		H.append([S[i],f[i]])
		H = sorted(H, key=lambda H: H[1])

		print 'this is H',H
		print
	while (len(H) > 2):
		# for k in range(n,2*n):

		# Place a zero at the end of f and s so that
		# when you run the code it doesn't say 'out of
		# index'
		f.append(0)
		S.append(0)
		print 'this is H',H
		print

		# l is the min freq value in H
		# it is a pair [char, freq]
		l = H[1]
		print 'this is l', l
		print
		
		# left is the left child of the tree.
		# it contains the same value as l
		left = Tree(H[1])
		H.remove(H[1])
		print 'this is left child',left.cargo
		print

		print 'this is H',H
		print

		# r is the 2nd min freq value in H
		# it is a pair [char, freq]
		r = H[1]
		print 'this is r',r
		print

		# right is the right child of the tree.
		# it contains the same values as r
		right = Tree(H[1])
		H.remove(H[1])
		print 'this is right child',right.cargo
		print

		# parent combines the two mins so that
		# [combined char, combined freq]
		parent = [l[0] + r[0], l[1] + r[1]]

		# tree sets a tree with a left child and right
		# child
		tree = Tree(parent, left, right)
		print 'this is parent',parent
		print

		# add the new parent node to H
		H.append(parent)

		# sort H based on the freq value
		H = sorted(H, key=lambda H: H[1])

		f[n+(n-len(H))-1] = l[1] + r[1]
		S[n+(n-len(H))-1] = l[0] + r[0]

		print 'this is f',f
		print
		print 'this is S',S
		print


	comb = []
	print 'this is n',n
	print
	for i in range(0,len(f)):
		comb.append([S[i],f[i]])
		print 'this is comb', comb
		print
		print 'this is i', i
		print

	# what is codebook T and how do I code it?
		

print huffmanEncode(S,f)

# def encodeString(x,T):
# 	y = []
# 	for i in range(1,len(x)+1)
# 		y = y + T[x[i]]
# 		return y

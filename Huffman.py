inputString="AAABBBBBBBBCCDEFFFFFFGIIIIJJz"
freqArray=[0]*26

def stringToFreq(stringInput):
    for char in stringInput:
        freqArray[ord(char.lower())-97] = freqArray[ord(char.lower())-97] + 1
        #print freqArray[ord(char.lower())-97]
        S=dict.fromkeys(stringInput).keys()
        S.sort()
    return freqArray, S

# print 2 arrays: the histogram and then number of unique 
# characters in the string, in lexicographical order
print stringToFreq(inputString)


def huffmanEncode(S,f):  
        H = []
        n = len(f)
        for i in range(1,n+1):
                H.insert(i,f[i])
        for k in range(n+1,2*n):
                i = H.deletemin(), j = H.deletemin()
                create a node numbered k with children i,j
                f[k] = f[i] + f[j]
                H.insert(k,f[k])

        create and return codebook T


inputString="AAABBBBBBBBCCDEFFFFFFGIIIIJJz"
freqArray=[0]*26
unique = []
def stringToFreq(stringInput):
    for char in stringInput:
        freqArray[ord(char.lower())-97] = freqArray[ord(char.lower())-97] + 1
        #print freqArray[ord(char.lower())-97]
    return freqArray, sorted(sorted(stringInput), key=str.upper)

# print the histogram and unique characters in the string, in lexographical order
print stringToFreq(inputString)

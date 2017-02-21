inputString="AAABBBBBBBBCCDEFFFFFFGIIIIJJz"
freqArray=[0]*26
def stringToFreq(stringInput):
    for char in stringInput:
        freqArray[ord(char.lower())-97] = freqArray[ord(char.lower())-97] + 1
        #print freqArray[ord(char.lower())-97]
    return freqArray


print stringToFreq(inputString)



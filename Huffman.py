inputString="AAABBBBBBBBCCDEFFFFFFGIIIIJJz"
freqArray=[0]*26

def stringToFreq(stringInput):
    for char in stringInput:
        freqArray[ord(char.lower())-97] = freqArray[ord(char.lower())-97] + 1
        #print freqArray[ord(char.lower())-97]
        a = dict.fromkeys(stringInput).keys()        
    return freqArray, sorted(sorted(a), key=str.lower)

# print the histogram and unique characters in the string, in lexographical order
print stringToFreq(inputString)

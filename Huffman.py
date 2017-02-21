inputString="AAABBBBBBBBCCDEFFFFFFGIIIIJJz"
freqArray=[0]*26

def stringToFreq(stringInput):
    for char in stringInput:
        freqArray[ord(char.lower())-97] = freqArray[ord(char.lower())-97] + 1
        #print freqArray[ord(char.lower())-97]
        S = dict.fromkeys(stringInput).keys()   
        S.sort()
    return freqArray, S

# print the histogram and unique characters in the string, in lexographical order
print stringToFreq(inputString)

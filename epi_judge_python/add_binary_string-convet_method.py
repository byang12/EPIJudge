# CHP 5 - 3.plus_one on p43 variant, Leetcode: 67. Add Binary
# convert binary str to Int, then convert back to str
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def convertBinaryToInt(a: str) ->int:
            i = len(a) - 1
            bitPointer = 1
            strSum = 0
            while i>=0:
                if a[i] == '1':
                    strSum = strSum + bitPointer
                bitPointer = bitPointer << 1
                i = i - 1
            return strSum
            
        abSum = convertBinaryToInt(a) + convertBinaryToInt(b)
        newStr = ''
        if abSum == 0:
            return '0'
        while abSum > 0:
            if abSum & 1:
                newStr = '1' + newStr
            else:
                newStr = '0' + newStr
            abSum = abSum >> 1
            
        return newStr

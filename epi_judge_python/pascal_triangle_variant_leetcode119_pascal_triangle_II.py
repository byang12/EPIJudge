class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]*(rowIndex+1)
        currentElement = 1
        for i in range(rowIndex):
            currentElement = currentElement*(rowIndex-i)//(i+1)
            result[i+1] = currentElement
        return result

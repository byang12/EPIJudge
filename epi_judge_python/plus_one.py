# CHP 5 - 3.plus_one on p43, not found in the epi judge, 
# Tested on Leetcode,
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        carry = 1
        while i >= 0:
            digits[i] = digits[i] + carry
            if not digits[i] == 10:
                carry = 0
                break
            digits[i] = 0
            i = i - 1
            
        if carry == 1:
            digits.insert(0, 1)
        
        return digits

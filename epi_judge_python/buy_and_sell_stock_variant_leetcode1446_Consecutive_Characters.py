class Solution:
    def maxPower(self, s: str) -> int:
        max_length = 1
        current_length = 1
        previous_element = s[0]
        for i in range(1,len(s)):
            if s[i] == previous_element:
                current_length = current_length + 1
            else:
                max_length = max(max_length,current_length)
                current_length = 1           
            previous_element = s[i]
        max_length = max(max_length,current_length)
        return max_length

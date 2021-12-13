class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        
        k = 0
        i = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k = k + 1
                
        return k

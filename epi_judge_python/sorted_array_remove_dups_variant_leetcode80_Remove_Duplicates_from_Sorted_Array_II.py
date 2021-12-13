class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        elementCount = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k = k + 1
                elementCount = 1
            else:
                if elementCount < 2:
                    nums[k] = nums[i]
                    k = k + 1
                elementCount = elementCount + 1
        return k

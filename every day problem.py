class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        result = 0
        smollNikita = list(accumulate(nums))
        bigNikita = sum(nums)
        for i in range(len(nums) - 1):
             if smollNikita[i] >= bigNikita - smollNikita[i]:
                result += 1   
        return result 

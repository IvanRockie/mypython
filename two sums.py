class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment_map = {}  
        
        for index, num in enumerate(nums):
            
            complement = target - num
            
            
            if complement in compliment_map:
                return [compliment_map[complement], index]
            
            
            compliment_map[num] = index

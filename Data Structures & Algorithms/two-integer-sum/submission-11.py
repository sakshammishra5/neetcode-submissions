class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compMap={}

        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in compMap:
                return [compMap[diff],i]
            else:
                compMap[nums[i]]=i
        return []   
        
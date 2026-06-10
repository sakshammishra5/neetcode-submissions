class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        sum_list=[]
        while i<len(nums):
            j=i+1
            while j <len(nums):
                if nums[i] + nums[j] == target:
                    sum_list.append(i)
                    sum_list.append(j)
                    return sum_list
                else:
                    j+=1
            i+=1
        return []            

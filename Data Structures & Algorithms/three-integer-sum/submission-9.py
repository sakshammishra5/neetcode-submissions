class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums=sorted(nums)
        res=[]

        for f in range(len(nums)):
            i=f+1
            j=len(nums)-1
            if nums[f]>0 :
                break
            if f>0 and nums[f]==nums[f-1]:
                continue
            while i<j:
                target_sum=nums[f]+nums[i]+nums[j]
                if target_sum > 0:
                    j=j-1
                elif target_sum < 0:
                    i=i+1
                else:
                    res.append([nums[f],nums[i],nums[j]])
                    i=i+1
                    j=j-1
                   
                    while i<j and nums[j]==nums[j+1]:
                        j=j-1
                    while i<j and nums[i]==nums[i-1]:
                        i=i+1

        
        return res
        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_list=sorted(nums)
        count=1
        longest=1
        for i in range(len(nums)-1):
            if sorted_list[i+1]==sorted_list[i]+1:
                count+=1

            elif sorted_list[i+1]==sorted_list[i]:
                continue

            else:
                longest=max(longest,count)
                count=1

        longest=max(longest,count)       
        
        return longest

             
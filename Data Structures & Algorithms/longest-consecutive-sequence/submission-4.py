class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_list=sorted(nums)
        count=1
        longest=1
        for i in range(len(nums)-1):
            if sorted_list[i+1]==sorted_list[i]+1:#peche element mein 1 plus karke agar agge wale ke barabar ata hai toh count badha denge
                count+=1

            elif sorted_list[i+1]==sorted_list[i]:#agar do element same hue to ingnore karenge loop ko continue kar ke
                continue

            else:
                longest=max(longest,count) # longest updated
                count=1  #count ko 1 se update kardenge kyuki sequence break ho gaya 

        longest=max(longest,count)   #loop khatam hone ke baad bhi longest ko update kar denge    
        
        return longest

             
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        i=0

        while i<=len(nums)-1:
            product=1
            j=0
            while j<=len(nums)-1:
                if i!=j:
                     product=nums[j]*product
                     j+=1
                else:
                    j+=1
            output.append(product)
            i+=1
        return output

                
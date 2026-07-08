class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        left=0
        right=n-1
        max_area=0

        while left<right:
            current_area=(right-left) * min(heights[left],heights[right])
            max_area=max(current_area,max_area)
           
            if heights[left]>heights[right]:
                right=right-1
            else:
                left=left+1
        

        return max_area
        
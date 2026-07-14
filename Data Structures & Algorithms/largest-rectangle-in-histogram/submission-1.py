class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        stack=[]
        left=[0]*n
        right=[0]*n
        res=[0]*n

        # findig left smallest value which will stack from left

        for i in range(n-1,-1,-1):
            while(stack and heights[stack[-1]]>heights[i]):
                left[stack[-1]]=i
                stack.pop()
            
            stack.append(i)
        
        # edge agar satck mein element bache hai aur
        while(stack):
            left[stack[-1]]=-1
            stack.pop()

        
        # finding right smallest from right-> to left
        for i in range(n):
            while(stack and heights[stack[-1]]>heights[i]):
                right[stack[-1]]=i
                stack.pop()
            
            stack.append(i)
        
        while(stack):
            right[stack[-1]]=n
            stack.pop()

        # finding the area 
        # Area= (left_smallest-right_smallest-1)*heights[i]

        for i in range(n):
            res[i]=(right[i]-left[i]-1)*heights[i]

        return max(res)
        
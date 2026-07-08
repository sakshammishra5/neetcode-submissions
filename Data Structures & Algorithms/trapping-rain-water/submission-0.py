class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left =[1]*n
        right=[1]*n

        left[0]=0
        right[n-1]=0
        max_left=height[0]
        max_right=height[n-1]
        res=[]

        for i in range(1,n,1):
            max_left=max(max_left,height[i])
            left[i]=max_left
        
        for i in range(n-1,0,-1):
            max_right=max(max_right,height[i])
            right[i]=max_right

        for i in range(n):
            min_h=min(left[i],right[i])
            water=min_h-height[i]

            if water<0:
                res.append(0)
            else:
                res.append(water)
        
        return sum(res)
    


        
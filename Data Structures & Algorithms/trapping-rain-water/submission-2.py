class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        max_right=0
        max_right_index=0
        water=0

        for i in range(n):
            if height[i]>max_right:
                max_right=height[i]
                max_right_index=i
        
        # solving for the left side 
        max_left=height[0]
        for i in range(1,max_right_index,1):
            if height[i-1]>max_left:
                max_left=height[i-1]
            min_left_right_building=min(max_left,max_right)
            if min_left_right_building>height[i]:
                water+= min_left_right_building-height[i]
        # solving for the right
        max_left=max_right
        max_left_index=max_right_index
        max_right=height[n-1]

        for i in range(n-2,max_left_index,-1):
            if height[i+1]>max_right:
                max_right=height[i+1]
            min_left_right_building=min(max_left,max_right)
            if min_left_right_building>height[i]:
                water+= min_left_right_building-height[i]

        return water
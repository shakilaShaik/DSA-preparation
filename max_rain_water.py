class Solution:
    def maxArea(self, height: List[int]) -> int:
        minHeight=0
        max_water=0
        for i in range(len(height)):
            water_level=0
            for j in range(i+1,len(height)):


                water_level=min(height[i],height[j]) * (j-i)
               
                max_water=max(max_water, water_level)
        return max_water

    
# optimised 


class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_water=0
        s=len(height)
        left=0
        right=len(height)-1
        

        while left <right:
            water_level=min(height[left],height[right]) * (right- left)
            max_water=max(water_level,max_water)
            if height[left] <height[right]:
                left=left+1
            else:
                right=right-1
        return max_water

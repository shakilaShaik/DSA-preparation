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

    

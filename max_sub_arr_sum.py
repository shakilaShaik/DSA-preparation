class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        maxSum=nums[0]
        j=1
        sum=nums[0]
    
        while j <n:
            sum=sum+nums[j]

            print('sum is ' , sum)
            if sum <nums[j]:
                sum=nums[j]
            
            maxSum= max(maxSum, sum)
            j=j+1
        return maxSum


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newDict={}
        for  i in  range(len(nums)):
            compliment = target-nums[i]
         
            if compliment in newDict:
                return [newDict[compliment],i]
            newDict[nums[i]]=i




// here the main aim is to find the target indices that adds up to target.
// newDict[nums[i]] =i safely stores the number nums[i] in the valid index i.
// assigning is possible in dictionaries where as , the empty arrays dont follow, we have to append the elements in the array.

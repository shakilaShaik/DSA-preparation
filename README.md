# DSA-preparation
The git repo is about all the DSA problems that i practiced and coded.

1. The longest substring without repeating  characters and  the length of the substring
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        charSet=set()
        max_length=0
        
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left+=1
            charSet.add(s[right])
            max_length= max(max_length, right-left+1)

        return max_length
                

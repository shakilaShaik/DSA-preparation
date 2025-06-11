class Solution:
   def lengthOfLongestSubstring(self, s: str) -> int:
       left=0
       long_str=set()
       max_len=0
       for right in range(len(s)):
           while(s[right] in long_str):
               long_str.remove(s[left])
               left +=1
           long_str.add(s[right])
           max_len=max(max_len, right-left+1)
       return max_len  

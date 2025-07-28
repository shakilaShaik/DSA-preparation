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



# Bruteforce approach
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len=0
        for i in range(len(s)):
            new_str=''
            for j in range(i,len(s)):
                if s[j] in new_str:
                    break
                
                else:
                    new_str=new_str+s[j]
                    print(new_str,"new str is")
                
                    new_len =len(new_str)
                    max_len=max(max_len,new_len)
                
        return max_len      

                


        

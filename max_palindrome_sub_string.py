class Solution:
    def longestPalindrome(self, s: str) -> str:
        pal_string=""
        max_pal=""
        n=len(s)
        for i in range(n):
            for j in range(i,n):
                string=s[i:j+1]
                if string==string[::-1] and len(string)>len(max_pal):
                    max_pal=string
        return max_pal
       
             

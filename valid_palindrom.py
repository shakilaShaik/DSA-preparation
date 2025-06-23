class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
  
        s = re.sub(r'[^a-z0-9]', '', s)
        print(s)
        left=0
        right=len(s)-1
        
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right -=1 
                
        return True
    

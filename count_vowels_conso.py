class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels_dict={}
        cons_dict={}
        max_count=0
        max_count_c=0
        for char in s:
            
            if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
                vowels_dict[char] =vowels_dict.get(char,0)+1
            else:
               

                cons_dict[char] =cons_dict.get(char,0) +1
        for i in vowels_dict:
          
            count=vowels_dict[i] 
            max_count=max(count, max_count)
           
        for j in cons_dict:
            count_c=cons_dict[j]
          
            max_count_c=max(count_c,max_count_c)
           
        return max_count + max_count_c                    

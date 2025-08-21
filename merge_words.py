 def mergeAlternately(self, word1: str, word2: str) -> str:
        newStr=""
        i=0
        j=0
       
        while(i <len(word1) and j<len(word2)):

            newStr =newStr+word1[i]
            i=i+1
            if i !=j:
                newStr=newStr+word2[j]
                j=j+1
        while(i<len(word1)):
            newStr=newStr+word1[i]
            i=i+1
        while(j<len(word2)):
            newStr=newStr+word2[j]
            j=j+1
        
       
        return newStr


//simple logic
newStr=newStr+word1[i]
newStr=newStr+word2[j]
i=i+1
j=j+1

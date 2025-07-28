s="shammu"

# length=len(s)
for i in range(len(s)):
    sub=""
    print("i is" , i)
    for j in range(i,len(s)):
        sub=sub+s[j]
        print("substrings are", sub)
        j=j+1
    i=i+1

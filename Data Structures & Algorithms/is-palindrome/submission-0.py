class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=s.replace(" ","")
        for a in s:
            if not a.isalnum():
                s=s.replace(a,"") 
        i,j=0,len(s)-1
        while (i<=j):
            if(s[i]!=s[j]):
                return False
            i+=1
            j-=1
        return True
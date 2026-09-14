class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr=""
        for c in s:
            if c.isalnum():
                newStr+=c.lower()
        rev=""
        n=len(newStr)
        for i in range(n-1,-1,-1):
            rev+=newStr[i]
        if rev==newStr:
            return True
        else:
            return False

        
        
        
        
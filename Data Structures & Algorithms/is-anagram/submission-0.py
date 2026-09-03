class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dici1={}
        dici2={}
        for ch in s:
            if ch in dici1:
                dici1[ch]+=1
            else:
                dici1[ch]=1
        for ch in t:
            if ch in dici2:
                dici2[ch]+=1
            else:
                dici2[ch]=1
        if dici1==dici2:
            return True
        else:
            return False
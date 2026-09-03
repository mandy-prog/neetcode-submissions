class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       dici={}
       for words in strs:
         key=" ".join(sorted(words))
         if key not in dici:
            dici[key]=[]
         dici[key].append(words)
       return list(dici.values())

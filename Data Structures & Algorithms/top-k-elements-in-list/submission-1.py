class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    dici={}
    for i in nums:
        if i in dici:
            dici[i]+=1
        else:
            dici[i]=1
    arr=sorted(dici,key=dici.get,reverse=True)
    return arr[:k]

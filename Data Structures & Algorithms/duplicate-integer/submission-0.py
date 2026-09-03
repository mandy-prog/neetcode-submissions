class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      n=len(nums)
      duplicate=[]
      s=False
      for i in range(n):
        if nums[i] in duplicate:
            s=True
        else:
            duplicate.append(nums[i])
      return s

       

        


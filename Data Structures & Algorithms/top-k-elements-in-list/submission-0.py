class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      count={}
      for i in nums:
        count[i]=1+count.get(i,0)
      res=[]
      for i in count:
        res.append([count[i],i])
      res.sort()
      res1=[]
      while len(res1)<k:
        
        res1.append(res.pop()[1])
      return res1



       
        


       
            
        
        
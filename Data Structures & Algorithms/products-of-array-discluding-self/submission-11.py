class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
       
        flag1=False
        count=0
        prod=1
        for i in nums:
            if i:
                prod*=i
            else:
                count+=1
        if count>1:
            return [0]*len(nums)
        for i in nums:
            if i==0 and count==1:
                res.append(prod)
            if i!=0 and count==1:
                res.append(0)
            if i!=0 and count==0:
                res.append(prod//i)
        return res

           
           
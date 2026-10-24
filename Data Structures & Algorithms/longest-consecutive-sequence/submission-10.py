class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        pointer=0
        result=0
        for i,n in enumerate(nums):
            
            if i==0:
                pointer=nums[i]
                count+=1
            if pointer+1==n:
                pointer+=1
                count+=1
            if pointer==n:
                continue
            if n>pointer+1:
                if count>result:
                    result=count
                    count=1
                else:
                    count=1
                pointer=n
            if(count>result):
                result=count
        
        if count>result:
            result=count
            
        return result


        
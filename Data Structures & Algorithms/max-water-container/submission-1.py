class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result=0
        i=0
        j=len(heights)-1
        while i<j:
            print(heights[i],heights[j])
            k=min(heights[i],heights[j])*abs(i-j)
            if k>result:
                result=k
            if heights[i]<heights[j]:
                i+=1
            elif heights[j]<heights[i]:
                j-=1
            else:
                i+=1
                j-=1
        return result
            

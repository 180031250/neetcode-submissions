class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        k=temperatures.copy()
        k.sort()
        max1=k[-1]
        for i,n in enumerate(temperatures):
            j=i+1
            count=1
            flag=False
            if n>=max1:
                result[i]=0
                continue
            
            while j<len(temperatures):
                
                if temperatures[j]>n:
                    
                    flag=True
                    break
                count+=1
                
                j+=1
            
            if flag==True:
                result[i]=count
            elif flag==False:
                result[i]=0
        return result




            

            

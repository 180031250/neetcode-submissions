class Solution:

    def encode(self, strs: List[str]) -> str:
        
        result=[]
        for i in strs:
           result.append(str(len(i)))
           result.append('#')
           result.append(i)
        
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result=[]
        i=0
        j=0
        print(s)
        while j!=len(s):
            
            i=j
            while s[j]!='#':
                j+=1
            len1=int(s[i:j])
            i=j+1
            result.append(s[i:j+len1+1])
            j=i+len1
            
        return result

       
       

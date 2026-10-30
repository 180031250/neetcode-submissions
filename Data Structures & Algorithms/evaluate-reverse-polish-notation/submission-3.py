class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l=[]
        k=0
        for i in tokens:
            if i=="+":
                
                r=l[-2]+l[-1]
                l.pop()
                l.pop()
                
                l.append(r)
            elif i=="-":
                 
                r=l[-2]-l[-1]
                l.pop()
                l.pop()
                
                l.append(r)
            elif i=="*":
                
                r=l[-2]*l[-1]
                l.pop()
                l.pop()
                
                l.append(r)
            elif i=="/":
                r=int(l[-2]/l[-1])
                l.pop()
                l.pop()
                
                l.append(r)
            else:
                l.append(int(i))
            k+=1
        return l[0]

        
class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for i,n in enumerate(s):
           
           
            if n=="{" or n=="(" or n=="[":
                l.append(n)
           
            if n ==")":
                if len(l)==0:
                    return False
                brc=l.pop()
                if brc=="(":
                   continue
                else:
                    
                    return False

            elif n=="}":
                if len(l)==0:
                    return False
                brc=l.pop()
                if brc=="{":
                    continue
                else:
                    print("p2")
                    return False
            elif n=="]":
                if len(l)==0:
                    return False
                brc=l.pop()
                if brc=="[":
                    continue
                else:
                    return False
        if len(l)>0:
            return False
        return True
        

        
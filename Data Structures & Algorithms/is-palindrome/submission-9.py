class Solution:
    def isPalindrome(self, s: str) -> bool:
        result=True
        s=s.lower()
        p1=0
        p2=len(s)-1
        alpha_num=[48,49,50,51,52,53,54,55,56,57]
        for i in range(97,123):
            alpha_num.append(i)
        while p1!=p2:
            p1_flag=False
            p2_flag=False
            

            while p1_flag==False:
                if p2==0 or p1==len(s)-1 or p1>p2:
                    return True
                if ord(s[p1]) not in alpha_num :
                     p1+=1
                else:
                    p1_flag=True
            
            while p2_flag==False:
                if p2==0 or p1==len(s)-1 or p1>p2:
                    return True
                if ord(s[p2]) not in alpha_num :
                        p2-=1
                else:
                    p2_flag=True
            

            print(p1,p2)
            print(s[p1],s[p2])
            if p2==0 or p1==len(s)-1 or p1>p2:
                return True
            if s[p1]!= s[p2]:
                return False
            
            p1+=1
            p2-=1
            
        return True
        
class MinStack:

    def __init__(self):
        self.minstack=[]
        self.min_value=10000000000000000000000
                      
        self.min_val=[]
       
        
        

    def push(self, val: int) -> None:
        self.minstack.append(val)
        if val<self.min_value or len(self.minstack)==1:
            self.min_value=val
        self.min_val.append(self.min_value)
        

    def pop(self) -> None:
        k=self.minstack.pop()
        self.min_val.pop()
        if k==self.min_value and len(self.min_val)!=0:
            self.min_value=self.min_val[-1]

        


    def top(self) -> int:
        
        return self.minstack[-1]

    def getMin(self) -> int:
        
       
        return self.min_val[-1]       

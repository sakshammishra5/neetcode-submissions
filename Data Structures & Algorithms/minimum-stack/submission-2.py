class MinStack:

    def __init__(self):
        self.stack=[]
         

    def push(self, val: int) -> None:
        if self.stack:
            minimum= self.stack[-1][1]
            if isinstance(val,int):
                minimum=min(minimum,val)
                self.stack.append((val,minimum))
        else:
            self.stack.append((val,val))
        

    def pop(self) -> None:
        if len(self.stack)==0:
            return "Stack is empty!"

        self.stack.pop()
        return None
        

    def top(self) -> int:
        top=None
        top=self.stack[-1]
        return top[0]
        
        

    def getMin(self) -> int:
        if len(self.stack)==0:
            return "stack is empty! fill the stack to run getMin"
        
        temp=self.stack[-1]
        min_val=temp[1]

        return min_val

        # minimum=self.stack[-1][1]
        # return minimum
        

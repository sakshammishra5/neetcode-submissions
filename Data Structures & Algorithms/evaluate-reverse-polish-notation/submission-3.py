class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==0:
            return -1

        stack =[]
        for s in range(len(tokens)):
            if tokens[s] not in {"+", "-", "*", "/"}:
                stack.append(int(tokens[s]))
            
            elif tokens[s]=="+":
                temp1=stack.pop()
                temp2=stack.pop()
                result=int(temp1)+int(temp2)
                stack.append(result)

            elif tokens[s]=="-":
                temp1=stack.pop()
                temp2=stack.pop()
                result=int(temp2)-int(temp1)
                stack.append(result)
            
            elif tokens[s]=="*":
                temp1=stack.pop()
                temp2=stack.pop()
                result=int(temp1)*int(temp2)
                stack.append(result)
            
            elif tokens[s]=="/":
                temp1=stack.pop()
                temp2=stack.pop()
                result=int(temp2)/int(temp1)
                stack.append(result)

        return int(stack.pop())


        
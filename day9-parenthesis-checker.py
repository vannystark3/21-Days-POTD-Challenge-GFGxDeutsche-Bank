class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here
        top = -1
        s = []
        l = len(x)
        for i in range(l):
            if(top==-1 and (x[i]==')'or x[i]==']' or x[i]=='}')):
                return False
            elif(x[i]=='(' or x[i]=='{' or x[i]=='['):
                s.append(x[i])
                top += 1
            elif((x[i]==')' and s[top]=='(') or (x[i]==']' and s[top]=='[') or (x[i]=='}' and s[top]=='{')):
                s.pop()
                top -= 1
            elif((x[i]==')' and s[top]!='(') or (x[i]==']' and s[top]!='[') or (x[i]=='}' and s[top]!='{')):
                return False
        # print(len(s))
        if(top!=-1):
            return False
        else:
            return True

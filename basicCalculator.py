# Will loop through string to and get the number
# will keep two variable summ and sign
# if we encounter opening bracket we will append current summ and sign to stack
# if we encounter closing bracket we pop summ and sign from stack and add to current summ


class Solution:
    def basicCalulator(self, s: str) -> int:
        sign = 1
        stack = []
        summ = 0
        i = 0
        
        while i < len(s):
            if s[i] >= '0' and s[i] <= '9':
                num = 0
                while s[i] >= '0' and s[i] <= '9':
                    num = num*10 + (ord(s[i]) - ord('0'))
                    i += 1
                summ += num*sign
                
            if s[i] == '+':
                sign = 1
            if s[i] == '-':
                sign = -1
            
            if s[i] == '(':
                stack.append(summ)
                stack.append(sign)
                summ = 0
                sign = 1
            
            if s[i] == ')':
                before_sign = stack.pop()
                before_summ = stack.pop()
                
                summ = summ*before_sign
                summ += before_summ
            i += 1
        return summ
            
obj1 = Solution()
s1 = "4+(6+10)+11+(10-1)"
print(obj1.basicCalulator(s1))

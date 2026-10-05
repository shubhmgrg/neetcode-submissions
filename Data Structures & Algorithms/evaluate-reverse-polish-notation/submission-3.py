class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                if i == '+':
                    stack.append(a + b)
                elif i == '*':
                    stack.append(a * b)
                elif i == '/':
                    c = abs(b) // abs(a)
                    if (b < 0 and a > 0) or (a < 0 and b > 0):
                        c = -c
                    stack.append(c)
                elif i == '-':
                    stack.append(b - a)

        return stack.pop()
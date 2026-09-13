class Solution:
    def isValid(self, s: str) -> bool:
        b = []

        for a in s:
            if a in '({[':
                b.append(a)
            else:
                if len(b) == 0:
                    return False


                match a:
                    case ')':
                        if b[-1] != '(':
                            return False
                        else:
                            b.pop()
                    case ']':
                        if b[-1] != '[':
                            return False
                        else:
                            b.pop()
                    case '}':
                        if b[-1] != '{':
                            return False
                        else:
                            b.pop()
        
        if len(b) == 0:
            return True
        return False
                        
                        
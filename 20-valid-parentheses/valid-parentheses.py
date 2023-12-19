class Solution:
    def isValid(self, s: str) -> bool:
        
        parantheses = list(s)
        stack = []

        for currentParanthese in parantheses:
            
            
            if (currentParanthese == "(" or currentParanthese == "{" or currentParanthese == "["):
                stack.append(currentParanthese)
                continue

            else:
                if (len(stack) == 0):
                    return False
                
                latestParanthese = stack.pop()

                if (latestParanthese == "(" and currentParanthese == ")"):
                    continue
                elif (latestParanthese == "[" and currentParanthese == "]"):
                    continue
                elif (latestParanthese == "{" and currentParanthese == "}"):
                    continue
                else:
                    return False
        
        if (len(stack) != 0): 
            return False
        
        return True
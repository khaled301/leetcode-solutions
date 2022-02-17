# Time Complexity = O(n)
# Space Complexity = O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        bracket_stack = deque()
        openning_bracket_list = ['(', '{', '[']
        ending_brackets = { 
            ')': '(', 
            '}': '{', 
            ']': '[' 
        }
        
        for i in range(len(s)):
            if s[i] in openning_bracket_list:
                bracket_stack.append(s[i])
            elif s[i] in ending_brackets:
                tempBracket = bracket_stack.pop() if 0 < len(bracket_stack) else ''
                
                if tempBracket != ending_brackets[s[i]]: return False
        
        if(len(bracket_stack) > 0): return False
        else: return True
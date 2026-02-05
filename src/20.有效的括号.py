class Solution:
    def isValid(self, s: str) -> bool:
        mp = {')':'(', '}':'{', ']':'['}
        stack = []

        for char in s:
            if char in mp:
                t = stack.pop() if stack else '#' 
                if t != mp[char]:
                    return False
            else:
                stack.append(char)
        return not stack
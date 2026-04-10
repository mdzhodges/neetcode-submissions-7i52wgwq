class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        valid_chars ={')': '(', '}': '{', ']':'['}

        for i in s:
            if i in valid_chars.values():
                stack.append(i)

            else:
                if len(stack) < 1:
                    return False
                val = stack.pop()
                if val != valid_chars[i]:
                    return False

        if len(stack) > 0:
            return False
        return True
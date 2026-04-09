class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned = ""
        for i in s:
            if i.isalnum():
                cleaned += i.lower()



        print(cleaned)
        for i in range(len(cleaned)):
            if cleaned[i] != cleaned[len(cleaned)-i-1]:
                return False
        
        return True
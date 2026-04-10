class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(t) > len(s):
            return ""

        t_dict = {}
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
        
        required = len(t_dict)
        window = {}
        formed = 0             
        
        ans = float("inf"), None, None
        
        l, r = 0, 0
        while r < len(s):
            char = s[r]
            window[char] = window.get(char, 0) + 1
            
            if char in t_dict and window[char] == t_dict[char]:
                formed += 1
            
            while l <= r and formed == required:
                char = s[l]
                
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                window[char] -= 1
                if char in t_dict and window[char] < t_dict[char]:
                    formed -= 1
                
                l += 1
            
            r += 1
            
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left, right = 0,len(s1)
        s_2_window = Counter(s2[left:right])
        s1_dict = Counter(s1)
        while right < len(s2):
            if s_2_window == s1_dict:
                return True
            s_2_window[s2[left]] -= 1
            s_2_window[s2[right]] = s_2_window.get(s2[right], 0) + 1

            right += 1
            left += 1
            

        if s_2_window == s1_dict:
            return True
            
        return False
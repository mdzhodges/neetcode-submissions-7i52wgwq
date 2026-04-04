class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_s = {}
        char_t = {}
        for i in range(len(t)):
            if t[i] in char_t:
                char_t[t[i]] += 1
            else:
                char_t[t[i]] = 1

        for i in range(len(s)):
            if s[i] in char_s:
                char_s[s[i]] += 1
            else:
                char_s[s[i]] = 1


        return char_s == char_t
            
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_change = 0
        changes = {}
        max_char_count = 0


        for right in range(len(s)):
            changes[s[right]] = changes.get(s[right], 0) + 1

            max_char_count = max(max_char_count, changes[s[right]])

            if (right - left + 1) - max_char_count > k:
                changes[s[left]] -= 1
                left += 1

            max_change = max(max_change, right - left + 1)

        return max_change
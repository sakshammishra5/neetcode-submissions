class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = 0
        max_count = 0
        result = 0
        count = {}

        for right in range(n):
            char = s[right]                              # character, index nahi
            count[char] = count.get(char, 0) + 1
            max_count = max(max_count, count[char])

            window_length = right - left + 1
            while window_length - max_count > k:
                count[s[left]] -= 1                       # yahan bhi character
                left += 1
                window_length = right - left + 1           # yeh line missing thi

            result = max(result, window_length)

        return result
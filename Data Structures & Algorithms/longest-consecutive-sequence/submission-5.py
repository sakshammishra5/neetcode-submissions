
        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)       # O(n): Convert to set for O(1) lookups
        longest = 0

        for n in num_set:         # Loop through each number
            # Only start counting if 'n' is the BEGINNING of a sequence
            if (n - 1) not in num_set:
                length = 1
                # Count forward: n+1, n+2, n+3...
                while (n + length) in num_set:
                    length += 1
                
                longest = max(longest, length)

        return longest
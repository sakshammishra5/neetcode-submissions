class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

    # prefix pass: answer[i] = product of everything LEFT of i
        prefix = 1
        for i in range(n):
            answer[i] = prefix       # write BEFORE multiplying, so i itself is excluded
            prefix *= nums[i]

    # suffix pass: multiply in product of everything RIGHT of i
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix      # combine left product with right product
            suffix *= nums[i]

        return answer
        
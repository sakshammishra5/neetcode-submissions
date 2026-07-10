class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []  # stores (temp, index), decreasing order

        for i in range(n):
            while stack and temperatures[i] > stack[-1][0]:
                top_temp, top_idx = stack.pop()
                result[top_idx] = i - top_idx
            stack.append((temperatures[i], i))

        return result
        
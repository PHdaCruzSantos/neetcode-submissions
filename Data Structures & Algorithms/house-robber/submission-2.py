class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i >= len(nums):
                return 0
            robbed = nums[i] + dfs(i + 2)
            cache[i] = max(dfs(i +1), robbed)
            return cache[i]
        return max(dfs(0), dfs(1))
            
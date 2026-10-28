class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums.sort()
        hash = dict()
        for i in range(len(nums)):
            if nums[i] in hash:
                return [hash[nums[i]], i]
            diff = target - nums[i]
            hash[diff] = i

        return []
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        h = set(nums)

        for i in range(len(nums) + 1):
            if i not in h:
                return i